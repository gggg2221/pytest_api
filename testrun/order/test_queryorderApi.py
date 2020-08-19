#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests,os, sys
from pytest_api.config import setting
from pytest_api.comzt.readexcel import ReadExcel
from pytest_api.comzt.writeexcel import WriteExcel
from pytest_api.comzt.sendrequests import SendRequests as r
import allure
import pytest

#获取测试数据
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
testData = ReadExcel(setting.SOURCE_FILE, "cloudorder").read_data()
# test_data = get_csv_data(testData)

@allure.epic('订单服务')
@allure.feature("订单查询")
class TestQueryOrder(object):
    """订单查询"""

    @classmethod
    def setup(self):
        self.s = requests.session()

    @classmethod
    def teardown(self):
        pass


    @allure.story("订单查询场景")
    # @pytest.mark.flaky(reruns=3,reruns_delay=3)
    @pytest.mark.parametrize('data',testData)
    def test_Queryorder(self, data):
        # 获取ID字段数值，截取结尾数字并去掉开头0
        rowNum = int(data['ID'].split("_")[1])
        print("******* 正在执行用例 ->{0} *********".format(data['ID']))
        print("请求方式: {0}，请求URL: {1}".format(data['method'], data['url']))
        print("请求参数: {0}".format(data['params']))
        print("post请求body类型为：{0} ,body内容为：{1}".format(data['type'], data['body']))
        # 发送请求
        re = r().sendRequests(self.s, data)
        # 获取服务端返回的值
        self.result = re.json()
        print("页面返回信息：%s" % re.content.decode("utf-8"))
        # 获取excel表格数据的状态码和消息
        readData_code = int(data["status_code"])
        readData_msg = data["msg"]
        if readData_code == self.result['resultCode'] and readData_msg == self.result['message']:
            OK_data = "PASS"
            print("测试结果: {0}---->{1}".format(data['ID'], OK_data))
            WriteExcel(setting.TARGET_FILE['orderresult']).write_data(rowNum + 1, OK_data)
        else:
            NOT_data = "FAIL"
            print("测试结果: {0}---->{1}", format(data['ID'], NOT_data))
            WriteExcel(setting.TARGET_FILE['orderresult']).write_data(rowNum + 1, NOT_data)
        # self.assertEqual(self.result['resultCode'], readData_code, "返回实际结果是->:%s" % self.result['resultCode'])
        assert self.result['resultCode']==readData_code, "返回实际结果是->:%s" % self.result['resultCode']


if __name__ == '__main__':
    pytest.main(['-s','test_queryorderApi.py'])
