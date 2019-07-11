#!/usr/bin/env python

import unittest
from common import kafkatools as k

class DkOrder(unittest.TestCase):
    def test_jsdk(self):
        # 发送出场数据
        k.kafkatools.send_out(k.dk_topic, k.js_outjson)

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
