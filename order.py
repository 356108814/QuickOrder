# coding:utf-8
import time
import threading
import config
from api import Api
from code import Code
from log import logger


class Order(object):
    def __init__(self):
        self.api = Api()
        self.code = Code(self.api)
        self.orders = []
        self.index = 0
    
    def start_check_orders(self):
        t = threading.Thread(target=self.check_orders, args=())
        t.start()
    
    def check_orders(self):
        while True:
            if self.is_can_check() or True:
                self.orders = self.api.get_orders("")
            if len(self.orders) > 0:
                logger.info(self.orders)
                break
            time.sleep(0.1)
    
    def is_can_check(self):
        now = time.localtime(time.time())
        hour = now.tm_hour
        minute = now.tm_min
        return hour >= 8 and (minute >= 59 or minute <= 3)
    
    def is_can_accept(self, order):
        return order and order['DistrictName'] in config.district_dict[config.account]

    def start_accept_order(self):
        while True:
            size = len(self.orders)
            if size > 0:
                logger.info('orders len:%s' % size)
                order = self.orders.pop()
                order_no = order['DecorationOrderNo']
                t = threading.Thread(target=self.submit_order, args=(order_no,))
                t.start()
                time.sleep(1)
    
    def submit_order(self, order_no):
        """
        经理抢单：需要设置人员workerDict，有验证码post，没验证码get
        非经理抢单：get 无验证码设置empty
        CurrentCustomer == '1007' ? 'ConstructorsChose(this)' : 'AcceptOrder(this)';
        :param order_no:
        :return:
        """
        is_post = False
        worker = ''
        code_id = 'empty'
        code_value = 'empty'
        code_config = self.api.get_validate_code_config(order_no)
        if code_config['Result']:
            is_validate = code_config['Data']['InputCode']
            if is_validate:
                code = self.code.get_validate_code(order_no)
                code_id = code['code_id']
                code_value = code['code_value']
        
        if config.is_manager(config.account):
            is_post = True
            # 设置施工人员
            worker = self.get_worker(order_no)
        
        response = self.api.accept_order(order_no, code_id, code_value, worker, is_post)
        if response and response['Result']:
            logger.info('================order success：%s %s' % (order_no, response))
        else:
            logger.info('================order failure %s:%s' % (order_no, response))
    
    def get_worker(self, order_no):
        """根据订单选择工友"""
        worker = ''
        require_positions = self.api.get_require_job_positions(order_no)
        print(require_positions)
        for p in require_positions:
            position_no = p['PositionNo']
            friends = self.api.get_friends(order_no, position_no)
            if len(friends) > 0:
                friend = friends[0]
                worker += '{0}-{1},'.format(position_no, friend['CustomerAccount'])
        worker = worker[0:len(worker) - 1]
        return worker
    
    def start_keep_login(self):
        t = threading.Thread(target=self.api.keep_login5, args=())
        t.start()
        
    def start_auto_order(self):
        while True:
            self.orders = self.api.get_orders("")
            if len(self.orders) > 0:
                logger.info(self.orders)
                break
            time.sleep(0.1)
        
        for order in self.orders:
            if not self.is_can_accept(order):
                continue
            logger.info('================start accept order ：%s ' % order)
            order_no = order['DecorationOrderNo']
            response = self.api.accept_order(order_no, 'empty', 'empty', 'empty', False)
            if response and response['Result']:
                logger.info('================order success：%s %s' % (order_no, response))
            else:
                logger.info('================order failure %s:%s' % (order_no, response))

        self.start_accept_order()
            

if __name__ == '__main__':
    o = Order()
    # o.start_check_orders()
    # o.start_accept_order()
    # o.orders = [{'DecorationOrderNo': 'M201804272771339'}, {'DecorationOrderNo': 'M201804272771336'}]
    # print(o.submit_order('M201805162941119'))
    # o.start_accept_order()
    # print(o.get_worker("M201805202975547"))
    o.start_auto_order()
