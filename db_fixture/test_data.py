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

    # 订单测试数据
    'cloud_order_copy': [
        {'id': 1, 'casename': '订单反查2', 'classname': 'orderfc2',
         'data': '{"serviceId":"fc.park.pay.query","attributes":{"parkCode":"20181213001","orderNo":"BK1e2bdd983ec342dd8752c78a5541b7"}}'}
    ]
}

# 要清楚数据的表名
table_name="cloud_order_copy"


# 测试数据插入表
def init_data():
    DB.init_data(datas)

# 清除测试数据
def clear_data():
    DB.clear(table_name)
