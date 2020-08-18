#!/usr/bin/env python

import requests,os,sys
from pytest_api.config import setting
from pytest_api.comzt.readexcel import ReadExcel
from pytest_api.comzt.writeexcel import WriteExcel
from pytest_api.comzt.sendrequests import SendRequests as r
import allure
import pytest

#获取测试数据
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
testData = ReadExcel(setting.SOURCE_FILE, "signnew").read_data()

@allure.epic('验签服务')
@allure.feature("验签")
class TestNewSign(object):
    """新验签"""

    def setup(self):
        self.s = requests.session()

    def teardown(self):
        pass

    @allure.story("渠道验签")
    @pytest.mark.parametrize('data',testData)
    def test_Signnisv(self,data):
        # 获取ID字段数值，截取结尾数字并去掉开头0
        rowNum = int(data['ID'].split("_")[1])
        print("******* 正在执行用例 ->{0} *********".format(data['ID']))
        print("请求方式: {0}，请求URL: {1}".format(data['method'], data['url']))
        print("请求参数: {0}".format(data['params']))
        print("post请求body类型为：{0} ,body内容为：{1}".format(data['type'], data['body']))

        #发送验签请求
        re=r().postRequests(data)
        print("页面返回信息：%s" % re.content.decode("utf-8"))
        self.result = re.json()

        # 取出验签状态结果进行校验
        # 获取excel表格数据的状态码和消息
        readData_code = int(data["status_code"])
        if readData_code == self.result['dataItems'][0]['isSignatory']:
            OK_data = "PASS"
            print("测试结果: {0}---->{1}".format(data['ID'], OK_data))
            WriteExcel(setting.TARGET_FILE['signresult']).write_data(rowNum + 1, OK_data)
        else:
            NOT_data = "FAIL"
            print("测试结果: {0}---->{1}".format(data['ID'], NOT_data))
            WriteExcel(setting.TARGET_FILE['signresult']).write_data(rowNum + 1, NOT_data)
        assert self.result['dataItems'][0]['isSignatory']==readData_code, "返回实际结果是->:%s" % self.result['dataItems'][0]['isSignatory']


if __name__ == '__main__':
    pytest.main(['-s', 'test_newsignApi.py'])