# coding:utf-8
import requests
import json


class Api(object):
    def __init__(self):
        self.baseUrl = 'http://twk.qk365.com'
        self.session = self.login()

    def request(self, url, data, is_post=True):
        if is_post:
            resp = self.session.post(url, data)
        else:
            resp = self.session.get(url=url, params=data)
        content = resp.content.decode('utf-8')
        print(content)
        return json.loads(content)

    def login(self):
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

    def keep_login(self):
        url = self.baseUrl + '/Account/KeepLogin'
        result = self.request(url, {}, False)
        return result

    def get_validate_code_config(self, order_no):
        url = self.baseUrl + '/WaitAcceptOrder/GetValidateCodeConfig'
        data = {"orderNo": order_no}
        return self.request(url, data, False)

    def get_validate_code(self):
        data = []
        url = self.baseUrl + '/WaitAcceptOrder/GetValidateCode'
        result = self.request(url, {}, False)
        for img_data in result['Data']['imgDatas']:
            data.append(img_data)
        return {"code_id": result['Data']['imgId'], "data": data}

    def get_friend(self, order_no, position_no):
        """
        选择工友
        :param order_no:
        :param position_no:
        :return: {"Result": true, "Data": [{"CustomerAccount": 1, "CustomerName": ""}]}
        """
        url = self.baseUrl + '/WaitAcceptOrder/GetCurrPositionFriends'
        data = {"positionNo": position_no, "decorationOrderNo": order_no}
        return self.request(url, data, True)

    def get_all_friend(self):
        """
        CustomerAccount（手机号）、CustomerName、JobPositionNo、PositionName
        :return:
        """
        url = self.baseUrl + '/Friends/GetDecorationFriendsInMappingSearch'
        data = {"NameOrTelmun": ""}
        return self.request(url, data, True)

    def get_orders(self, page_size=100):
        """
        :param page_size:
        :return: {"Result":true,"Message":"","Data":{"TotalRecords":0,"PageSize":100,"TotalPage":0,"CurrentPage":1,"ItemList":[]}}
        """
        orders = []
        url = self.baseUrl + '/WaitAcceptOrder/WaitAcceptOrderQuery'
        data = {"CurrentPage": 1, "PageSize": page_size, "CityNameDistrictName": ""}
        response = self.request(url, data)
        if response['Result']:
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
        # workerDatastr += (positionNo + "-" + customerAccount + ",");
        worker_data_str = ""
        worker_dict = worker_data_str[0:len(worker_data_str) - 1]
        url = self.baseUrl + '/WaitAcceptOrder/AcceptOrder'
        data = {"orderNo": order_no, "validCodeId": code_id, "validCodeValue": code_value, "workerDict": worker}
        return self.request(url, data, is_post)


if __name__ == '__main__':
    api = Api()
    # print(api.get_all_friend())
    # print(api.get_friend("M201804272771339", 9037))
    print(api.get_orders())
    # print(api.keep_login())
