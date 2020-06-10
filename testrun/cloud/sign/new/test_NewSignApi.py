#!/usr/bin/env python

import unittest, requests, ddt,re, os, sys,json
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
        # 获取ID字段数值，截取结尾数字并去掉开头0
        rowNum = int(data['ID'].split("_")[1])
        #获取请求数据,转为json
        sign_data=data['body']
        sign_json=json.loads(sign_data)

        #生成验签反查密钥
        from comzt import publicdef as p
        sign=p.Publicdef.setmd5(sign_json)

        #发送验签请求
        rpo=r().PostRequests(self.s, c.SIGN_URL, sign_json, sign)
        #检索验签状态,返回list数据
        # self.result=rpo.findall(r'.*\"isSignatory\":(.+?)',rpo,re.M|re.I)
        #取出验签状态结果进行校验
        # self.assertTrue(int(result[0])== 1, "验签成功")
        self.result = rpo
        # 获取excel表格数据的状态码和消息
        readData_code = int(data["status_code"])
        readData_msg = data["msg"]
        if readData_code == self.result['resultCode'] and readData_msg == self.result['message']:
            OK_data = "PASS"
            print("用例测试结果: {0}---->{1}".format(data['ID'], OK_data))
            WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1, OK_data)
        else:
            NOT_data = "FAIL"
            print("用例测试结果: {0}---->{1}", format(data['ID'], NOT_data))
            WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1, NOT_data)
        self.assertEqual(self.result['resultCode'], readData_code, "返回实际结果是->:%s" % self.result['resultCode'])



if __name__ == '__main__':
    unittest.main()
