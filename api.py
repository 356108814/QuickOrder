# coding:utf-8
import requests
import json
import time
import config
from log import logger


class Api(object):
    def __init__(self):
        self.baseUrl = 'http://twk.qk365.com'
        self.session = self.login()

    def request(self, url, data, is_post=True):
        response = None
        if is_post:
            resp = self.session.post(url, data)
        else:
            resp = self.session.get(url=url, params=data)
        try:
            content = resp.content.decode('utf-8')
            response = json.loads(content)
            logger.debug('response: %s %s %s' % (url, data, response))
        except Exception as e:
            response = None
            logger.error(response)
        return response

    def login(self):
        data = {
            'CustomerAccount': config.account,
            'Password': config.pwd
        }
        login_url = self.baseUrl + '/Account/Login'
        # 设置请求头
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
        # 构造Session
        session = requests.Session()
        # 在session中发送登录请求，此后这个session里就存储了cookie
        # 可以用print(session.cookies.get_dict())查看
        resp = session.post(login_url, data)
        return session

    def keep_login5(self):
        while True:
            response = self.keep_login()
            if not response['Result']:
                self.login()
            time.sleep(5)

    def keep_login(self):
        url = self.baseUrl + '/Account/KeepLogin'
        result = self.request(url, {}, False)
        return result

    def get_customer_info(self):
        """
        reponse['Data'] == '1007' 为经理
        :return:
        """
        url = self.baseUrl + '/WaitAcceptOrder/GetCustomerInfo'
        response = self.request(url, {'CurrentPage': 1, 'PageSize': 15}, True)
        return response

    def get_validate_code_config(self, order_no):
        url = self.baseUrl + '/WaitAcceptOrder/GetValidateCodeConfig'
        data = {"orderNo": order_no}
        return self.request(url, data, False)

    def get_validate_code(self):
        data = []
        url = self.baseUrl + '/WaitAcceptOrder/GetValidateCode'
        result = self.request(url, {}, False)
        if result:
            for img_data in result['Data']['imgDatas']:
                data.append(img_data)
            return {"code_id": result['Data']['imgId'], "data": data}
        return {"code_id": "empty", "data": "empty"}

    def get_friends(self, order_no, position_no):
        """
        根据订单和工种选人员
        :param order_no:
        :param position_no:
        :return: [{"CustomerAccount": 1, "CustomerName": ""}]
        """
        url = self.baseUrl + '/WaitAcceptOrder/GetCurrPositionFriends'
        data = {"positionNo": position_no, "decorationOrderNo": order_no}
        response = self.request(url, data, True)
        if response and response['Result']:
            return response['Data']
        return []

    def get_all_friend(self):
        """
        CustomerAccount（手机号）、CustomerName、JobPositionNo、PositionName
        :return:
        """
        url = self.baseUrl + '/Friends/GetDecorationFriendsInMappingSearch'
        data = {"NameOrTelmun": ""}
        return self.request(url, data, True)

    def get_orders(self, district_name='', page_size=100):
        """
        :return: {"Result":true,"Message":"","Data":{"TotalRecords":0,"PageSize":100,"TotalPage":0,"CurrentPage":1,"ItemList":[]}}
        """
        orders = []
        url = self.baseUrl + '/WaitAcceptOrder/WaitAcceptOrderQuery'
        data = {"CurrentPage": 1, "PageSize": page_size, "CityNameDistrictName": ''}
        response = self.request(url, data)
        if response is not None and response['Result']:
            orders = response['Data']['ItemList']
        return orders

    def get_require_job_positions(self, order_no):
        """
        订单必选职位
        :param order_no:
        :return: [{'PositionNo': 1, 'PositionName': ''}]
        """
        url = self.baseUrl + '/WaitAcceptOrder/GetRequireJobPositions'
        response = self.request(url, {'decorationOrderNO': order_no}, True)
        if response['Result']:
            return response['Data']
        return []

    def accept_order(self, order_no, code_id="empty", code_value="empty", worker="", is_post=True):
        url = self.baseUrl + '/WaitAcceptOrder/AcceptOrder'
        data = {"orderNo": order_no, "validCodeId": code_id, "validCodeValue": code_value, "workerDict": worker}
        return self.request(url, data, is_post)


if __name__ == '__main__':
    api = Api()
    # print(api.get_all_friend())
    # print(api.get_friend("M201804272771339", 9037))
    # print(api.get_orders())
    # print(api.keep_login())
    # print(api.get_customer_info())
    # print(api.get_validate_code_config("M201805202975547"))
    print(api.get_require_job_positions("M201805202975547"))
