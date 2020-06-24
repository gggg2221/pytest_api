#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
TEST_CONFIG =  os.path.join(BASE_DIR,"config","dbconfig.ini")
# 测试用例模板文件
# SIGN_FILE=os.path.join(BASE_DIR,"testcase","signTestCase.xlsx")
# ORDER_FILE=os.path.join(BASE_DIR,"testcase","orderTestCase.xlsx")
# SOURCE_FILE={'signcase':SIGN_FILE,'ordercase':ORDER_FILE}
SOURCE_FILE=os.path.join(BASE_DIR,"testcase","CloudApiTestCase.xlsx")


# excel测试用例结果文件
SIGN_RESULT = os.path.join(BASE_DIR,"report","excelReport","signTestCaseResult.xlsx")
ORDER_RESULT = os.path.join(BASE_DIR,"report","excelReport","orderTestCaseResult.xlsx")
TARGET_FILE = {'signresult':SIGN_RESULT,'orderresult':ORDER_RESULT}

# TARGET_FILE = os.path.join(BASE_DIR,"report","excelReport","signTestCaseResult.xlsx")
# 测试用例报告
TEST_REPORT = os.path.join(BASE_DIR,"report")
# 测试用例程序文件
TEST_CASE = os.path.join(BASE_DIR,"testrun")

# print(TEST_CASE)