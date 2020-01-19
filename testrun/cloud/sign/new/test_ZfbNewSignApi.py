#!/usr/bin/env python

import unittest,requests,json,re
from comzt import condata as c
from comzt import publicdef as p
from comzt import sendrequests as s

class ZfbNewSign(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    def test_ZfbnIsv(self):

        #生成验签反查密钥

        sign=p.Publicdef().setmd5(c.zfb_signnjson)
        # print(sign)

        #发送验签请求
        rpo=s.SendRequests().postrequests(self.s, c.SIGN_URL, c.zfb_signnjson, sign)

        #检索验签状态,返回list数据
        result=re.findall(r'.*\"isSignatory\":(.+?)',rpo,re.M|re.I)

        #取出验签状态结果进行校验
        self.assertTrue(int(result[0])== 1, "验签成功")



if __name__ == '__main__':
    unittest.main()
