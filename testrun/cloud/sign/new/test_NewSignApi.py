#!/usr/bin/env python

import unittest, requests, ddt,re, os, sys
from config import setting
from comzt.readexcel import ReadExcel
from comzt.writeexcel import WriteExcel
from comzt import condata as c
from comzt.sendrequests import SendRequests as r

#获取测试数据
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
testData = ReadExcel(setting.SOURCE_FILE, "signnew").read_data()

@ddt.ddt
class NewSign(unittest.TestCase):
    """新验签"""

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    @ddt.data(*testData)
    def test_Wxnisv(self,data):

        postjson=str(data['body'])
        zfb=list(postjson)
        print(zfb)
        #生成验签反查密钥
        from comzt import publicdef as p
        sign=p.Publicdef.setmd5(c.zfb_signnjson)

        #发送验签请求
        rpo=r().PostRequests(self.s, c.SIGN_URL, c.zfb_signnjson, sign)

        #检索验签状态,返回list数据
        result=re.findall(r'.*\"isSignatory\":(.+?)',rpo,re.M|re.I)

        #取出验签状态结果进行校验
        self.assertTrue(int(result[0])== 1, "验签成功")



if __name__ == '__main__':
    unittest.main()
