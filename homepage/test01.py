import struct
import datetime
from django_redis import get_redis_connection
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meet.settings")#  项目名称
django.setup()

import requests


def locatebyLatLng(lat, lng, pois=0):
    '''
    根据经纬度查询地址
    '''
    items = {'location': str(lat) + ',' + str(lng), 'ak': 'XhDg0CerOl020ANVfHnl6aaXs4o47Au9', 'output': 'json'}
    res = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items)
    result = res.json()
    # print(result)
    # print('--------------------------------------------')
    #result = result['result']['formatted_address'] + ',' + result['result']['sematic_description']
    # result_site = result['result']['addressComponent']['city']
    result_s = result['result']['formatted_address']

    return result_s



conn = get_redis_connection('default')

x = locatebyLatLng(lat=123, lng=23)


def geoadd(lng, lat, sites):

    add_site = conn.geoadd('site', lng, lat, sites) # 增加位置信息
    return '添加成功'
# print(geoadd('116.28000233597092', '39.6679994936725', 'buzhidao'))


def geopos( site2):
    user_msg = conn.geopos('site',  site2) #显示坐标位置信息
    return user_msg
# print(geopos( 'beijing'))


def geodist(site1, site2):
    user_distance = conn.geodist('site', site1, site2, 'm') # 计算两地之间的距离
    return user_distance
# print(geodist('chengdu', 'beijing'))


def georadiusbymember(condition, num):
    user_radius = conn.georadiusbymember('site', condition, num, 'm', 'withdist') # 计算范围内的距离
    for i in user_radius:
        print(i[0].decode())
    return user_radius

# x = georadiusbymember('北京市大兴区魏永路', 100)
# print(x)


# name = str(input('请输入您的姓名：'))
# birth_day = int(input('请输入您的出生日期：”'))
# age = datetime.date.today().month
# print(age)


