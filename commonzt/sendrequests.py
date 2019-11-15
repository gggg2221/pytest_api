#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os, sys, json

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class SendRequests():
    """发送请求数据"""

    # 通用请求
    def sendRequests(self, s, apiData):
        try:
            # 从读取的表格中获取响应的参数作为传递
            method = apiData["method"]
            url = apiData["url"]
            if apiData["params"] == "":
                par = None
            else:
                par = eval(apiData["params"])
            if apiData["headers"] == "":
                h = None
            else:
                h = eval(apiData["headers"])
            if apiData["body"] == "":
                body_data = None
            else:
                body_data = eval(apiData["body"])
            type = apiData["type"]
            v = False
            if type == "data":
                body = body_data
            elif type == "json":
                body = json.dumps(body_data)
            else:
                body = body_data

            # 发送请求
            re = s.request(method=method, url=url, headers=h, params=par, data=body, verify=v)

            return re
        except Exception as e:
            print(e)

    # 自定义post方法
    def postRequests(self,s, urls, jsonData, sign):

        # 发送表单请求并获取响应内容
        # re = json.loads((s.post(url=urls, data={'key': json.dumps(jsonData, ensure_ascii=False), 'sign': sign},
        #             headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})).text)
        re =(s.post(url=urls, data={'key': json.dumps(jsonData, ensure_ascii=False), 'sign': sign},
                                headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})).text

        return re
