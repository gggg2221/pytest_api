#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os,sys

from testrun.sign.test_newsignApi import NewSign

sys.path.append(os.path.dirname(__file__))
from config import setting
import unittest,time
from comzt.sendmail import send_mail
from comzt.newReport import new_report
from db_fixture import test_data
from package.HTMLTestRunner import HTMLTestRunner

def add_case(test_path=setting.TEST_CASE):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='*Api.py')
    return discover

def run_case(all_case,result_path=setting.TEST_REPORT):
    """执行所有的测试用例"""

    # 初始化接口测试数据
    # test_data.clear_data()
    # test_data.init_data()


    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = result_path + '/' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='云平台接口自动化测试报告',description='后台服务',tester='zt')
    runner.run(all_case)
    fp.close()
    # 调用模块生成最新的报告
    report = new_report(setting.TEST_REPORT)
    # 调用发送邮件模块
    # send_mail(report)

if __name__ =="__main__":

    case=add_case()
    run_case(case)