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
    # order_no = 'M201804272771339'
    # qiang = Qiang()
    # qiang.session = qiang.login()
    # # orders = qiang.get_orders()
    # # code = qiang.get_validate_code_config("M201804272771339")
    # # code = qiang.get_validate_code()
    # result = qiang.accept_order(order_no)
    # print(result)
    import time
    import calendar
    
    now = time.localtime(time.time())
    print(now)
    
    a = [{'BalconyCount': 2, 'CorridorCount': 1, 'Latitude': '30.389499', 'TransactionNumber': 11940,
          'AcceptProgress': 0, 'Cancel': 0, 'District': '54', 'FeedAgainFlag': 0, 'Province': '43',
          'CurrentUserAcceptDate': None, 'ExpectEndDate': None, 'DistrictName': '余杭区', 'IsMaterialFlag': 0,
          'Longitude': '120.309173', 'OrderStatus': 200, 'DelegateUser': None, 'HouseTypeName': '毛坯房', 'ProPicPath': '',
          'ProvinceName': '浙江省', 'Layout': '4房-2卫-1厨-2阳台-0厅-1走廊', 'Published': 45,
          'DecorationOrderNo': 'M201805212984698', 'ExpectStartDate': None, 'CustomerName': None, 'DelayDay': 0,
          'IsPMwriteBackCompleted': False, 'DecorationEndDate': None, 'DecorationStartDate': None, 'KitchenCount': 1,
          'InDate': '2018-05-21 14:39:55', 'RoomCount': 4, 'ProcedureDelayDaySum': 0, 'Telephone': None,
          'DeliveryDate': '2018-05-18 00:00:00', 'InUser': '工程自动审批开工', 'Unqualified': 0, 'HouseType': 1,
          'AcceptIngDate': '2018-05-21 14:39:55', 'IsDelegateFlag': 0, 'DelegateTime': None, 'Qualified': 0,
          'AcceptDate': None, 'CityName': '杭州市', 'Constructing': 0, 'HouseAddress': '杭州市余杭区******',
          'FinishConstructing': 0, 'Payed': 0, 'City': '44', 'IsWriteBackForAllCompleted': False,
          'IsDistrictCanAccept': 1, 'TotalCount': 45, 'OtherRoom': 0, 'AcceptUser': None, 'ZipPackagePath': None,
          'RoomNo': '900-022-961', 'WaitPublish': 0, 'Accepted': 0, 'TotalProgress': 45, 'WCCount': 2,
          'SubmitUserName': '工程自动审批开工', 'HallCount': 0},
         {'BalconyCount': 1, 'CorridorCount': 1, 'Latitude': '30.08945', 'TransactionNumber': 11943,
          'AcceptProgress': 0, 'Cancel': 0, 'District': '53', 'FeedAgainFlag': 0, 'Province': '43',
          'CurrentUserAcceptDate': None, 'ExpectEndDate': None, 'DistrictName': '萧山区', 'IsMaterialFlag': 0,
          'Longitude': '120.196202', 'OrderStatus': 200, 'DelegateUser': None, 'HouseTypeName': '毛坯房',
          'ProPicPath': 'http://oss-wuxi.qk365.com/qingkepic/M00/D5/0E/CgoKZ1r_3S6AOwEzABJwCGozTJo320.jpg',
          'ProvinceName': '浙江省', 'Layout': '4房-2卫-1厨-1阳台-0厅-1走廊', 'Published': 45,
          'DecorationOrderNo': 'M201805212984984', 'ExpectStartDate': None, 'CustomerName': None, 'DelayDay': 0,
          'IsPMwriteBackCompleted': False, 'DecorationEndDate': None, 'DecorationStartDate': None, 'KitchenCount': 1,
          'InDate': '2018-05-21 14:50:00', 'RoomCount': 4, 'ProcedureDelayDaySum': 0, 'Telephone': None,
          'DeliveryDate': '2018-05-17 00:00:00', 'InUser': '工程自动审批开工', 'Unqualified': 0, 'HouseType': 1,
          'AcceptIngDate': '2018-05-21 14:50:00', 'IsDelegateFlag': 0, 'DelegateTime': None, 'Qualified': 0,
          'AcceptDate': None, 'CityName': '杭州市', 'Constructing': 0, 'HouseAddress': '杭州市萧山区******',
          'FinishConstructing': 0, 'Payed': 0, 'City': '44', 'IsWriteBackForAllCompleted': False,
          'IsDistrictCanAccept': 1, 'TotalCount': 45, 'OtherRoom': 0, 'AcceptUser': None, 'ZipPackagePath': None,
          'RoomNo': '900-022-897', 'WaitPublish': 0, 'Accepted': 0, 'TotalProgress': 45, 'WCCount': 2,
          'SubmitUserName': '工程自动审批开工', 'HallCount': 0},
         {'BalconyCount': 2, 'CorridorCount': 2, 'Latitude': '31.069794', 'TransactionNumber': 11937,
          'AcceptProgress': 0, 'Cancel': 0, 'District': '11', 'FeedAgainFlag': 0, 'Province': '1',
          'CurrentUserAcceptDate': None, 'ExpectEndDate': None, 'DistrictName': '闵行区', 'IsMaterialFlag': 0,
          'Longitude': '121.501596', 'OrderStatus': 200, 'DelegateUser': None, 'HouseTypeName': '毛坯房',
          'ProPicPath': 'http://oss-wuxi.qk365.com/qingkepic/M00/D7/D6/CgoKaFsCL7qAW87rAAWz2IOHUjc133.jpg',
          'ProvinceName': '上海市', 'Layout': '3房-2卫-1厨-2阳台-0厅-2走廊', 'Published': 45,
          'DecorationOrderNo': 'M201805212983441', 'ExpectStartDate': None, 'CustomerName': None, 'DelayDay': 0,
          'IsPMwriteBackCompleted': False, 'DecorationEndDate': None, 'DecorationStartDate': None, 'KitchenCount': 1,
          'InDate': '2018-05-21 12:19:55', 'RoomCount': 3, 'ProcedureDelayDaySum': 0, 'Telephone': None,
          'DeliveryDate': '2018-05-17 00:00:00', 'InUser': '工程自动审批开工', 'Unqualified': 0, 'HouseType': 1,
          'AcceptIngDate': '2018-05-21 12:19:55', 'IsDelegateFlag': 0, 'DelegateTime': None, 'Qualified': 0,
          'AcceptDate': None, 'CityName': '上海市', 'Constructing': 0, 'HouseAddress': '上海市闵行区******',
          'FinishConstructing': 0, 'Payed': 0, 'City': '2', 'IsWriteBackForAllCompleted': False,
          'IsDistrictCanAccept': 0, 'TotalCount': 45, 'OtherRoom': 0, 'AcceptUser': None, 'ZipPackagePath': None,
          'RoomNo': '900-022-910', 'WaitPublish': 0, 'Accepted': 0, 'TotalProgress': 45, 'WCCount': 2,
          'SubmitUserName': '工程自动审批开工', 'HallCount': 0},
         {'BalconyCount': 2, 'CorridorCount': 1, 'Latitude': '31.387347', 'TransactionNumber': 11938,
          'AcceptProgress': 0, 'Cancel': 0, 'District': '37', 'FeedAgainFlag': 0, 'Province': '27',
          'CurrentUserAcceptDate': None, 'ExpectEndDate': None, 'DistrictName': '昆山市', 'IsMaterialFlag': 0,
          'Longitude': '121.0349', 'OrderStatus': 200, 'DelegateUser': None, 'HouseTypeName': '装修房',
          'ProPicPath': 'http://oss-wuxi.qk365.com/qingkepic/M00/D8/16/CgoKZ1sCSveAM-J5ABHbyZ2Tmno620.jpg',
          'ProvinceName': '江苏省', 'Layout': '3房-1卫-1厨-2阳台-0厅-1走廊', 'Published': 44,
          'DecorationOrderNo': 'M201805212983770', 'ExpectStartDate': None, 'CustomerName': None, 'DelayDay': 0,
          'IsPMwriteBackCompleted': False, 'DecorationEndDate': None, 'DecorationStartDate': None, 'KitchenCount': 1,
          'InDate': '2018-05-21 12:49:55', 'RoomCount': 3, 'ProcedureDelayDaySum': 0, 'Telephone': None,
          'DeliveryDate': '2018-05-17 00:00:00', 'InUser': '工程自动审批开工', 'Unqualified': 0, 'HouseType': 2,
          'AcceptIngDate': '2018-05-21 12:49:55', 'IsDelegateFlag': 0, 'DelegateTime': None, 'Qualified': 0,
          'AcceptDate': None, 'CityName': '苏州市', 'Constructing': 0, 'HouseAddress': '苏州市昆山市******',
          'FinishConstructing': 0, 'Payed': 0, 'City': '28', 'IsWriteBackForAllCompleted': False,
          'IsDistrictCanAccept': 0, 'TotalCount': 44, 'OtherRoom': 0, 'AcceptUser': None, 'ZipPackagePath': None,
          'RoomNo': '900-022-914', 'WaitPublish': 0, 'Accepted': 0, 'TotalProgress': 44, 'WCCount': 1,
          'SubmitUserName': '工程自动审批开工', 'HallCount': 0},
         {'BalconyCount': 3, 'CorridorCount': 1, 'Latitude': '30.668937', 'TransactionNumber': 11939,
          'AcceptProgress': 0, 'Cancel': 0, 'District': '156', 'FeedAgainFlag': 0, 'Province': '153',
          'CurrentUserAcceptDate': None, 'ExpectEndDate': None, 'DistrictName': '江岸区', 'IsMaterialFlag': 0,
          'Longitude': '114.337398', 'OrderStatus': 200, 'DelegateUser': None, 'HouseTypeName': '毛坯房',
          'ProPicPath': 'http://oss-wuxi.qk365.com/qingkepic/M00/C5/E4/CgoKaFr1bRmADam3ABQD1x8NeBw203.jpg',
          'ProvinceName': '湖北省', 'Layout': '4房-2卫-1厨-3阳台-0厅-1走廊', 'Published': 45,
          'DecorationOrderNo': 'M201805212984510', 'ExpectStartDate': None, 'CustomerName': None, 'DelayDay': 0,
          'IsPMwriteBackCompleted': False, 'DecorationEndDate': None, 'DecorationStartDate': None, 'KitchenCount': 1,
          'InDate': '2018-05-21 14:09:55', 'RoomCount': 4, 'ProcedureDelayDaySum': 0, 'Telephone': None,
          'DeliveryDate': '2018-05-09 00:00:00', 'InUser': '工程自动审批开工', 'Unqualified': 0, 'HouseType': 1,
          'AcceptIngDate': '2018-05-21 14:09:55', 'IsDelegateFlag': 0, 'DelegateTime': None, 'Qualified': 0,
          'AcceptDate': None, 'CityName': '武汉市', 'Constructing': 0, 'HouseAddress': '武汉市江岸区******',
          'FinishConstructing': 0, 'Payed': 0, 'City': '154', 'IsWriteBackForAllCompleted': False,
          'IsDistrictCanAccept': 0, 'TotalCount': 45, 'OtherRoom': 0, 'AcceptUser': None, 'ZipPackagePath': None,
          'RoomNo': '900-022-451', 'WaitPublish': 0, 'Accepted': 0, 'TotalProgress': 45, 'WCCount': 2,
          'SubmitUserName': '工程自动审批开工', 'HallCount': 0},
         {'BalconyCount': 1, 'CorridorCount': 1, 'Latitude': '', 'TransactionNumber': 11941, 'AcceptProgress': 0,
          'Cancel': 0, 'District': '29', 'FeedAgainFlag': 0, 'Province': '27', 'CurrentUserAcceptDate': None,
          'ExpectEndDate': None, 'DistrictName': '姑苏区', 'IsMaterialFlag': 0, 'Longitude': '', 'OrderStatus': 200,
          'DelegateUser': None, 'HouseTypeName': '毛坯房',
          'ProPicPath': 'http://oss-wuxi.qk365.com/qingkepic/M00/D8/5A/CgoKZ1sCZ--AfmpaABMBeqCQpwQ801.jpg',
          'ProvinceName': '江苏省', 'Layout': '4房-2卫-1厨-1阳台-0厅-1走廊', 'Published': 44,
          'DecorationOrderNo': 'M201805212984885', 'ExpectStartDate': None, 'CustomerName': None, 'DelayDay': 0,
          'IsPMwriteBackCompleted': False, 'DecorationEndDate': None, 'DecorationStartDate': None, 'KitchenCount': 1,
          'InDate': '2018-05-21 14:49:55', 'RoomCount': 4, 'ProcedureDelayDaySum': 0, 'Telephone': None,
          'DeliveryDate': '2018-05-17 00:00:00', 'InUser': '工程自动审批开工', 'Unqualified': 0, 'HouseType': 1,
          'AcceptIngDate': '2018-05-21 14:49:55', 'IsDelegateFlag': 0, 'DelegateTime': None, 'Qualified': 0,
          'AcceptDate': None, 'CityName': '苏州市', 'Constructing': 0, 'HouseAddress': '苏州市姑苏区******',
          'FinishConstructing': 0, 'Payed': 0, 'City': '28', 'IsWriteBackForAllCompleted': False,
          'IsDistrictCanAccept': 0, 'TotalCount': 44, 'OtherRoom': 0, 'AcceptUser': None, 'ZipPackagePath': None,
          'RoomNo': '900-022-895', 'WaitPublish': 0, 'Accepted': 0, 'TotalProgress': 44, 'WCCount': 2,
          'SubmitUserName': '工程自动审批开工', 'HallCount': 0},
         {'BalconyCount': 2, 'CorridorCount': 1, 'Latitude': '', 'TransactionNumber': 11942, 'AcceptProgress': 0,
          'Cancel': 0, 'District': '11', 'FeedAgainFlag': 0, 'Province': '1', 'CurrentUserAcceptDate': None,
          'ExpectEndDate': None, 'DistrictName': '闵行区', 'IsMaterialFlag': 0, 'Longitude': '', 'OrderStatus': 200,
          'DelegateUser': None, 'HouseTypeName': '毛坯房',
          'ProPicPath': 'http://oss-wuxi.qk365.com/qingkepic/M00/D3/8B/CgoKaFr-n6SAVO97ABLnwQzKt7U894.jpg',
          'ProvinceName': '上海市', 'Layout': '3房-2卫-1厨-2阳台-0厅-1走廊', 'Published': 45,
          'DecorationOrderNo': 'M201805212984933', 'ExpectStartDate': None, 'CustomerName': None, 'DelayDay': 0,
          'IsPMwriteBackCompleted': False, 'DecorationEndDate': None, 'DecorationStartDate': None, 'KitchenCount': 1,
          'InDate': '2018-05-21 14:49:57', 'RoomCount': 3, 'ProcedureDelayDaySum': 0, 'Telephone': None,
          'DeliveryDate': '2018-05-15 00:00:00', 'InUser': '工程自动审批开工', 'Unqualified': 0, 'HouseType': 1,
          'AcceptIngDate': '2018-05-21 14:49:57', 'IsDelegateFlag': 0, 'DelegateTime': None, 'Qualified': 0,
          'AcceptDate': None, 'CityName': '上海市', 'Constructing': 0, 'HouseAddress': '上海市闵行区******',
          'FinishConstructing': 0, 'Payed': 0, 'City': '2', 'IsWriteBackForAllCompleted': False,
          'IsDistrictCanAccept': 0, 'TotalCount': 45, 'OtherRoom': 0, 'AcceptUser': None, 'ZipPackagePath': None,
          'RoomNo': '900-022-738', 'WaitPublish': 0, 'Accepted': 0, 'TotalProgress': 45, 'WCCount': 2,
          'SubmitUserName': '工程自动审批开工', 'HallCount': 0},
         {'BalconyCount': 2, 'CorridorCount': 1, 'Latitude': '30.86943', 'TransactionNumber': 11944,
          'AcceptProgress': 0, 'Cancel': 0, 'District': '18', 'FeedAgainFlag': 0, 'Province': '1',
          'CurrentUserAcceptDate': None, 'ExpectEndDate': None, 'DistrictName': '奉贤区', 'IsMaterialFlag': 0,
          'Longitude': '121.570786', 'OrderStatus': 200, 'DelegateUser': None, 'HouseTypeName': '毛坯房',
          'ProPicPath': 'http://oss-wuxi.qk365.com/qingkepic/M00/D8/65/CgoKZ1sCa32ALhVXABKfZZY8bkk362.jpg',
          'ProvinceName': '上海市', 'Layout': '3房-1卫-0厨-2阳台-0厅-1走廊', 'Published': 44,
          'DecorationOrderNo': 'M201805212985147', 'ExpectStartDate': None, 'CustomerName': None, 'DelayDay': 0,
          'IsPMwriteBackCompleted': False, 'DecorationEndDate': None, 'DecorationStartDate': None, 'KitchenCount': 0,
          'InDate': '2018-05-21 14:59:56', 'RoomCount': 3, 'ProcedureDelayDaySum': 0, 'Telephone': None,
          'DeliveryDate': '2018-05-15 00:00:00', 'InUser': '工程自动审批开工', 'Unqualified': 0, 'HouseType': 1,
          'AcceptIngDate': '2018-05-21 14:59:56', 'IsDelegateFlag': 0, 'DelegateTime': None, 'Qualified': 0,
          'AcceptDate': None, 'CityName': '上海市', 'Constructing': 0, 'HouseAddress': '上海市奉贤区******',
          'FinishConstructing': 0, 'Payed': 0, 'City': '2', 'IsWriteBackForAllCompleted': False,
          'IsDistrictCanAccept': 0, 'TotalCount': 44, 'OtherRoom': 0, 'AcceptUser': None, 'ZipPackagePath': None,
          'RoomNo': '900-022-796', 'WaitPublish': 0, 'Accepted': 0, 'TotalProgress': 44, 'WCCount': 1,
          'SubmitUserName': '工程自动审批开工', 'HallCount': 0}]
