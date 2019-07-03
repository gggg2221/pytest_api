#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys, time, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db_fixture.mysql_db import DB

# 定义过去时间
past_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - 100000))
# 定义将来时间
future_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 10000))

# 创建测试数据
datas = {
    # 发布会表数据
    # 'sign_event':[
    #     {'id':1,'name':'红米Pro发布会','`limit`':2000,'status':1,'address':'北京会展中心','start_time':future_time},
    # ]

    # #　嘉宾表数据
    # 'sign_guest':[
    #     {'id':1,'realname':'Tom','phone':13511886601,'email':'alen@mail.com','sign':0,'event_id':1},
    # ]

    # 订单测试数据
    'cloud_order_copy': [
        {'id': 1, 'casename': '订单反查2', 'classname': 'orderfc2',
         'data': '{"serviceId":"fc.park.pay.query","attributes":{"parkCode":"20181213001","orderNo":"BK1e2bdd983ec342dd8752c78a5541b7"}}'}
    ]
}


# 测试数据插入表
def init_data():
    DB().init_data(datas)
