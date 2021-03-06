# coding:utf-8
import logging.handlers

LOG_FILE = 'order.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
# fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
fmt = '%(asctime)s - %(message)s'

formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter

logger = logging.getLogger('order')  # 获取名为tst的logger
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.DEBUG)

