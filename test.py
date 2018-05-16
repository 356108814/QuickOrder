# encoding: utf-8
import requests
import json


class Qiang(object):
    
    def __init__(self):
        self.session = None
    
    def request(self, url, data, is_post=True):
        """
        发送请求
        :param url:
        :param data:
        :param is_post:
        :return:
        """
        if is_post:
            resp = self.session.post(url, data)
        else:
            resp = self.session.get(url=url, params=data)
        content = resp.content.decode('utf-8')
        return json.loads(content)
    
    def login(self):
        """
        :return: session
        """
        data = {
            "CustomerAccount": "15357298885",
            "Password": ""
        }
        login_url = "http://twk.qk365.com/Account/Login"
        # 设置请求头
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
        # 构造Session
        session = requests.Session()
        # 在session中发送登录请求，此后这个session里就存储了cookie
        # 可以用print(session.cookies.get_dict())查看
        resp = session.post(login_url, data)
        return session
    
    def get_orders(self):
        url = "http://twk.qk365.com/WaitAcceptOrder/WaitAcceptOrderQuery"
        data = {"CurrentPage": 1, "PageSize": 15, "CityNameDistrictName": ""}
        return self.request(url, data)
    
    def get_validate_code_config(self, order_no):
        url = "http://twk.qk365.com/WaitAcceptOrder/GetValidateCodeConfig"
        data = {"orderNo": order_no}
        result = self.request(url, data, False)
        # result.Data.imgDatas[i]
        return {"code_id": result.Data.imgId}
    
    def get_validate_code(self):
        url = "http://twk.qk365.com/WaitAcceptOrder/GetValidateCode"
        data = {}
        result = self.request(url, data, False)
        for img in result['Data']['imgDatas']:
            print('<img src="data:image/png;base64,' + img + '">')
        return {"code_id": result['Data']['imgId']}
    
    def get_friends(self, order_no, position_no):
        url = "http://twk.qk365.com/WaitAcceptOrder/GetCurrPositionFriends"
        data = {"positionNo": order_no, "decorationOrderNo": position_no}
        return self.request(url, data, True)
    
    def accept_order(self, order_no, code_id="empty", code_value="empty"):
        url = "http://twk.qk365.com/WaitAcceptOrder/AcceptOrder"
        data = {"orderNo": order_no, "validCodeId": code_id, "validCodeValue": code_value, "workerDict": ""}
        return self.request(url, data, False)


if __name__ == '__main__':
    order_no = 'M201804272771339'
    qiang = Qiang()
    qiang.session = qiang.login()
    # orders = qiang.get_orders()
    # code = qiang.get_validate_code_config("M201804272771339")
    # code = qiang.get_validate_code()
    result = qiang.accept_order(order_no)
    print(result)
