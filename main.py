# coding:utf-8
from log import logger
from order import Order

if __name__ == '__main__':
    order = Order()
    order.start_check_orders()
    order.start_accept_order()
    order.start_keep_login()
