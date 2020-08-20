#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os,sys

sys.path.append(os.path.dirname(__file__))
import allure
import pytest
from pytest_api.comzt.sendmail import send_mail
from pytest_api.comzt.newReport import new_report
from pytest_api.db_fixture import test_data
from pytest_api.package.HTMLTestRunner import HTMLTestRunner

# def add_case(test_path=setting.TEST_CASE):
#     """加载所有的测试用例"""
#     discover = unittest.defaultTestLoader.discover(test_path, pattern='*Api.py')
#     return discover


@allure.step('执行所有用例')
def runcase():
    #--allure-epics
    #--allure-features
    #--allure-stories
    #--allure_severities=critical, blocker'
    #–workers(optional) *：多进程运行需要加此参数，  *是进程数。默认为1。
    #'--reruns=1','--reruns-delay=2','-m', 'fail',失败重跑一次，在每次开跑前会等待2s
    #--tests-per-worker(optional) *：多线程运行， *是每个worker运行的最大并发线程数。默认为1

    pytest.main(['-v','--allure-features=订单查询','--reruns=1','--reruns-delay=2','--alluredir','report/allure'])
    #生成html测试报告
    os.system("F:/allure-2.13.4/bin/allure.bat "
              "generate "
              "F:/workspace/pytest_api/report/result "
              "-o "
              "F:/workspace/pytest_api/report/html")


# def run_case(all_case,result_path=setting.TEST_REPORT):
    """执行所有的测试用例"""

    # 初始化接口测试数据
    # test_data.clear_data()
    # test_data.init_data()

    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # filename = result_path + '/' + now + 'result.html'
    # fp = open(filename,'wb')
    # runner = HTMLTestRunner(stream=fp,title='云平台接口自动化测试报告',description='后台服务',tester='zt')
    # runner.run(all_case)
    # fp.close()
    # 调用模块生成最新的报告
    # report = new_report(setting.TEST_REPORT)
    # 调用发送邮件模块
    # send_mail(report)


if __name__ =="__main__":
    runcase()
