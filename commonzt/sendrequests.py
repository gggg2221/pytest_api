#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os, sys, json
import requests
# import common.Contes
# from common import Session

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class SendRequests():

    """发送请求数据"""

    # def __init__(self):
    #     """
    #     :param env:
    #     """
    #     self.session =Session.Session()
    #     self.get_session = self.session.get_session(self)

    def get_request(self, url, data, header):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.get(url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.get(url=url, params=data, headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def post_request(self, url, data, header):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = (requests.post(url=url, headers=header, cookies=self.get_session)).text
            else:
                response = (requests.post(url=url, params=data, headers=header, cookies=self.get_session)).text

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

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

    # 自定义表单post方法
    def postRequests(self,s, urls, jsonData, sign):

        # 发送表单请求并获取响应内容
        # re = json.loads((s.post(url=urls, data={'key': json.dumps(jsonData, ensure_ascii=False), 'sign': sign},
        #             headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})).text)
        response =(s.post(url=urls, data={'key': json.dumps(jsonData, ensure_ascii=False), 'sign': sign},
                                headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})).text

        return response
