#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os, sys, json
import requests
from comzt import condata as c

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
    def sendRequests(self, s, apidata):
        try:
            # 从读取的表格中获取响应的参数作为传递
            method = apidata["method"]
            url = apidata["url"]
            if apidata["params"] == "":
                par = None
            else:
                par = eval(apidata["params"])
            if apidata["headers"] == "":
                h = None
            else:
                h = eval(apidata["headers"])
            if apidata["body"] == "":
                body_data = None
            else:
                body_data = eval(apidata["body"])
            type = apidata["type"]
            v = False
            if type == "data":
                body = body_data
            elif type == "json":
                body = json.dumps(body_data,ensure_ascii=False)
            else:
                body = body_data

            # 发送请求
            re = s.request(method=method, url=url, headers=h, params=par, data=body, verify=v)

            return re
        except Exception as e:
            print(e)

    # 自定义表单post方法--验签反查
    def postRequests(self, apidata):
        #取出数据
        method = apidata["method"]
        urls= apidata["url"]
        sign_data = apidata['body']
        sign_json = json.loads(sign_data)
        sign_json['data']['dataItems'][0]['inTime'] = c.iotime
        # 生成验签反查密钥
        from comzt import publicdef as p
        sign = p.Publicdef.setmd5(sign_json)

        # 发送表单请求并获取响应内容
        re =requests.request(method=method,url=urls,data={'key': json.dumps(sign_json, ensure_ascii=False), 'sign': sign},
                                headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})

        return re

        # 验签post方法--验签反查
    def postsign(self,s,url,signjson,sign):

        # 发送表单请求并获取响应内容
        re = requests.request(method='post', url=url,
                              data={'key': json.dumps(signjson, ensure_ascii=False), 'sign': sign},
                              headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})
        return re
