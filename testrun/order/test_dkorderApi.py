#!/usr/bin/env python

import pytest,requests,time
from comzt import kafkatools as k
from comzt import condata as c
from comzt.sendrequests import SendRequests as r
from comzt import publicdef as p
from db_fixture import mysql_db as m
import allure

@allure.epic('订单服务')
@allure.feature('代扣订单')
class TestDkOrder(object):

    def setup(self):
        self.s = requests.session()

    def teardown(self):
        pass

    #微信代扣
    @allure.story('微信代扣')
    def test_wxisv(self):
        sign=p.Publicdef.setmd5(c.js_signjson)
        # print(sign)
        #发送入场验签数据
        r().postRequests(self.s,c.SIGN_URL,c.js_signjson,sign)
        creattime = p.Publicdef.getdate()
        carno =c.WXCARNO
        # 等待验签完成
        time.sleep(2)

        k.kafkatools.send_out(c.DkTopic,c.js_outjson)
        time.sleep(5)
        sql = f'select ORDER_NO from cp_order_main where CAR_NO="{carno}" and ORDER_STATUS=0 and CREATE_TIME>="{creattime}" LIMIT 1'
        order=m.DB().select(sql)
        # print(order)
        assert order!=""


if __name__ == '__main__':
    pytest.main(['-s','test_dkorderApi.py'])
