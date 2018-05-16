# coding:utf-8

base_image_dir = 'G:/GitHub/QuickOrder/images'

friends = {
    "15357298885": [
        {'CustomerAccount': '13013196739', 'CustomerName': '', 'PositionName': '水电工', 'JobPositionNo': '9037'},
        {'CustomerAccount': '13739172711', 'CustomerName': '', 'PositionName': '水电工', 'JobPositionNo': '9037'},
        {'CustomerAccount': '13866087649', 'CustomerName': '', 'PositionName': '水电工', 'JobPositionNo': '9037'},
        {'CustomerAccount': '17356091203', 'CustomerName': '', 'PositionName': '水电工', 'JobPositionNo': '9037'},
        {'CustomerAccount': '18055629272', 'CustomerName': '', 'PositionName': '水电工', 'JobPositionNo': '9037'},
        {'CustomerAccount': '18133073252', 'CustomerName': '', 'PositionName': '水电工', 'JobPositionNo': '9037'},
        {'CustomerAccount': '18656598020', 'CustomerName': '', 'PositionName': '水电工', 'JobPositionNo': '9037'},
        {'CustomerAccount': '18726141571', 'CustomerName': '', 'PositionName': '水电工', 'JobPositionNo': '9037'},
        {'CustomerAccount': '13150062528', 'CustomerName': '', 'PositionName': '木工', 'JobPositionNo': '9038'},
        {'CustomerAccount': '18010714077', 'CustomerName': '', 'PositionName': '木工', 'JobPositionNo': '9038'},
        {'CustomerAccount': '18051310315', 'CustomerName': '', 'PositionName': '木工', 'JobPositionNo': '9038'},
        {'CustomerAccount': '18055620080', 'CustomerName': '', 'PositionName': '木工', 'JobPositionNo': '9038'},
        {'CustomerAccount': '18130528441', 'CustomerName': '', 'PositionName': '木工', 'JobPositionNo': '9038'},
        {'CustomerAccount': '18225566742', 'CustomerName': '', 'PositionName': '木工', 'JobPositionNo': '9038'},
        {'CustomerAccount': '18305569816', 'CustomerName': '', 'PositionName': '木工', 'JobPositionNo': '9038'},
        {'CustomerAccount': '18654068899', 'CustomerName': '', 'PositionName': '木工', 'JobPositionNo': '9038'},
        {'CustomerAccount': '13165966786', 'CustomerName': '', 'PositionName': '泥工', 'JobPositionNo': '9039'},
        {'CustomerAccount': '13225707878', 'CustomerName': '', 'PositionName': '泥工', 'JobPositionNo': '9039'},
        {'CustomerAccount': '13966547015', 'CustomerName': '', 'PositionName': '泥工', 'JobPositionNo': '9039'},
        {'CustomerAccount': '15205568229', 'CustomerName': '', 'PositionName': '泥工', 'JobPositionNo': '9039'},
        {'CustomerAccount': '17681268560', 'CustomerName': '', 'PositionName': '泥工', 'JobPositionNo': '9039'},
        {'CustomerAccount': '18055621729', 'CustomerName': '', 'PositionName': '泥工', 'JobPositionNo': '9039'},
        {'CustomerAccount': '18226461270', 'CustomerName': '', 'PositionName': '泥工', 'JobPositionNo': '9039'},
        {'CustomerAccount': '18509388333', 'CustomerName': '', 'PositionName': '泥工', 'JobPositionNo': '9039'},
        {'CustomerAccount': '13033174683', 'CustomerName': '', 'PositionName': '油漆工', 'JobPositionNo': '9040'},
        {'CustomerAccount': '13095567757', 'CustomerName': '', 'PositionName': '油漆工', 'JobPositionNo': '9040'},
        {'CustomerAccount': '13355567626', 'CustomerName': '', 'PositionName': '油漆工', 'JobPositionNo': '9040'},
        {'CustomerAccount': '13685569421', 'CustomerName': '', 'PositionName': '油漆工', 'JobPositionNo': '9040'},
        {'CustomerAccount': '13761893898', 'CustomerName': '', 'PositionName': '油漆工', 'JobPositionNo': '9040'},
        {'CustomerAccount': '15309661032', 'CustomerName': '', 'PositionName': '油漆工', 'JobPositionNo': '9040'},
        {'CustomerAccount': '17609402666', 'CustomerName': '', 'PositionName': '油漆工', 'JobPositionNo': '9040'},
        {'CustomerAccount': '18693812089', 'CustomerName': '', 'PositionName': '油漆工', 'JobPositionNo': '9040'}]
}

# 是否为经理
manager_dict = {
    '15357298885': True
}


def is_manager(account):
    return manager_dict[account + ''] is True


class Config(object):
    def __init__(self):
        pass
