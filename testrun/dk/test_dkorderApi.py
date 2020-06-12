#!/usr/bin/env python

import unittest,requests,time
from comzt import kafkatools as k
from comzt import condata as c
from comzt.sendrequests import SendRequests as r
from comzt import publicdef as p
from db_fixture import mysql_db as m


class DkOrder(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    #捷顺代扣
    def test_dkpub(self):
        sign=p.Publicdef.setmd5(c.js_signjson)
        # print(sign)
        #发送入场验签数据
        r().postrequests(self.s,c.SIGN_URL,c.js_signjson,sign)
        # 等待验签完成
        time.sleep(2)
        k.kafkatools.send_out(c.DkTopic,c.js_outjson)
        time.sleep(10)
        sql1 = "SELECT ORDER_NO from cs_biz_order where CAR_NO='藏-JK1111' and PAY_TYPE='WX' and status=0 ORDER BY CREATE_TIME DESC;"
        order=m.DB().select(sql1)
        # print(order)
        self.assertTrue(order!="","捷顺代扣成")


if __name__ == '__main__':
    unittest.main()
