#!/usr/bin/env python

import unittest,requests
from common import kafkatools as k
from common import condata as c
from common.sendrequests import SendRequests as r


class DkOrder(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    #捷顺代扣
    def test_jsdk(self):
        #发送入场验签数据
        r().postRequests(self.s,c.js_signjson,1111)

        # k.kafkatools.send_out(c.DkTopic, c.js_outjson)

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
