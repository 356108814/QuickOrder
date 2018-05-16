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
    
    def start_check_orders(self):
        t = threading.Thread(target=self.check_orders, args=())
        t.start()
    
    def check_orders(self):
        while True:
            self.orders = self.api.get_orders()
            if len(self.orders) > 0:
                logger.info(self.orders)
                break
            time.sleep(0.5)
    
    def is_can_accept(self, order):
        return True
    
    def start_accept_order(self):
        while len(self.orders) > 0:
            order = self.orders.pop()
            if self.is_can_accept(order):
                order_no = order['DecorationOrderNo']
                t = threading.Thread(target=self.submit_order, args=(order_no,))
                t.start()
    
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
            is_validate = True # code_config['Data']['InputCode']
            if is_validate:
                code = self.code.get_validate_code(order_no)
                code_id = code['code_id']
                code_value = code['code_value']
        
        if config.is_manager('15357298885'):
            is_post = True
            # 设置施工人员
            worker = self.get_worker(order_no)
        
        response = self.api.accept_order(order_no, code_id, code_value, worker, is_post)
        if response['Result']:
            logger.info('抢单成功：%s' % response)
        else:
            logger.info('%s抢单失败:%s' % (order_no, response['Message']))
    
    def get_worker(self, order_no):
        """根据订单选择工友"""
        worker = ''
        require_positions = self.api.get_require_job_positions(order_no)
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


if __name__ == '__main__':
    o = Order()
    # o.start_check_orders()
    # o.start_accept_order()
    # o.orders = [{'DecorationOrderNo': 'M201804272771339'}, {'DecorationOrderNo': 'M201804272771336'}]
    print(o.submit_order('M201804272771339'))
    # o.start_accept_order()
