#!/usr/bin/env python

import unittest,requests,time,json
from common import kafkatools as k
from common import condata as c
from common.sendrequests import SendRequests as r
from common import publicdef


class DkOrder(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    #捷顺代扣
    def test_jsdk(self):
        p=publicdef.publicdef()
        sign=p.setMd5(c.js_signjson)
        # print(sign)
        #发送入场验签数据
        r().postRequests(self.s,c.SIGN_URL,c.js_signjson,sign)
        # 等待验签完成
        time.sleep(2)
        k.kafkatools.send_out(c.DkTopic,c.js_outjson)

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
