# coding:utf-8
import time
from api import Api
from log import logger


class Order(object):
    def __init__(self):
        self.api = Api()
        self.orders = []

    def start_check(self):
        while True:
            self.orders = self.api.get_orders()
            if len(self.orders) > 0:
                logger.info(self.orders)
            time.sleep(1)

    def is_can_accept(self, order):
        return True

    def start_accept_order(self):
        while True:
            for order in self.orders:
                if self.is_can_accept(order):
                    order_no = order['DecorationOrderNo']
                    self.submit_order(order_no)
                    pass
            time.sleep(1)

    def submit_order(self, order_no):
        """
        CurrentCustomer == '1007' ? 'ConstructorsChose(this)' : 'AcceptOrder(this)';
        :param order_no:
        :return:
        """
        worker = self.get_worker(order_no)
        code_config = self.api.get_validate_code_config(order_no)
        if code_config['Result']:
            if code_config['Data']['InputCode']:
                code = self.get_validate_code()
                self.api.accept_order(order_no, code['code_id'], code['code_value'], worker, True)
            else:
                self.api.accept_order(order_no, 'empty', 'empty', worker, False)
        pass

    def get_worker(self, order_no):
        # 从好友中
        worker = ''
        response = self.api.get_friend(order_no)
        return worker

    def get_validate_code(self):
        code_id = 1
        code_value = ''
        return {'code_id': code_id, 'code_value': code_value}


if __name__ == '__main__':
    o = Order()
    o.start_check()
