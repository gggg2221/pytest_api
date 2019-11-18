#!/usr/bin/env python

import unittest,requests,json,re
from commonzt import condata as c
from commonzt import publicdef as p
from commonzt import sendrequests as s

class ZfbOldSign(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    def test_ZfboIsv(self):

        #生成签名数据
        sign=p.publicdef().setMd5(c.zfb_signojson)
        # print(sign)

        #发送验签请求
        rpo=s.SendRequests().postRequests(self.s, c.OldSIGN_URL, c.wx_signojson, sign)

        #检索验签状态,返回list数据
        result=re.findall(r'.*\"is_signatory\":(.+?)',rpo,re.M|re.I)

        # print(s)
        # print(s.SendRequests)
        # print(s.SendRequests())

        #取出验签状态结果进行校验
        self.assertTrue(int(result[0])== 1, "验签成功")



if __name__ == '__main__':
    unittest.main()
