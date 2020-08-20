#!/usr/bin/env python

import pytest,requests,time
from pytest_api.comzt import kafkatools as k
from pytest_api.comzt import condata as c
from pytest_api.comzt.sendrequests import SendRequests as r
from pytest_api.comzt import publicdef as p
from pytest_api.comzt import readconfig as read
from pytest_api.db_fixture import mysql_db as m
import allure

read=read.readconfig().read_config()
DkTopic=read['cloud']['dktopic']

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
        sign=p.Publicdef.setmd5(c.wx_signjson)
        #发送入场验签数据
        r().postsign(self.s,c.SIGN_URL,c.wx_signjson,sign)
        creattime = p.Publicdef.getdate()
        carno =c.WXCARNO
        # 等待验签完成
        time.sleep(2)
        k.Kafkatools().send_out(DkTopic,c.wxoutjson)
        time.sleep(3)
        sql = f'select ORDER_NO from cs_biz_order where CAR_NO="{carno}" and STATUS=0 and CREATE_TIME>="{creattime}" LIMIT 1'
        order=m.DB().select(sql)
        assert order!=""


if __name__ == '__main__':
    pytest.main(['-s','test_dkorderApi.py'])
