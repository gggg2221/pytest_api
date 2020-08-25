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

@allure.epic("一级标签")
@allure.feature("二级标签")
@allure.story("三级标签")
@allure.title("测试用例标题")
@allure.description("测试用例描述")
@allure.step("测试用例步骤")
#测试用例级别
#blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
#critical级别：临界缺陷（ 功能点缺失）
#normal级别：普通缺陷（数值计算错误）
#minor级别：次要缺陷（界面错误与UI需求不符）
#trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
@allure.severity(allure.severity_level.CRITICAL)


@allure.step('执行所有用例')
def runcase():
    #--allure-epics
    #--allure-features
    #--allure-stories
    #--allure_severities=critical, blocker'
    #–workers(optional) *：多进程运行需要加此参数，  *是进程数。默认为1。
    #'--reruns=1','--reruns-delay=2','-m', 'fail',失败重跑一次，在每次开跑前会等待2s
    #--tests-per-worker(optional) *：多线程运行， *是每个worker运行的最大并发线程数。默认为1

    pytest.main(['-v','--allure-features=订单查询','--alluredir','report/allure'])
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
