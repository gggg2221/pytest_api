# !/usr/bin/env python
from __future__ import print_function
import time, hashlib,json
import random as r
from comzt import condata as c


class Publicdef:

    #获取当前时间
    @staticmethod
    def getdate():
        # 获取当前时间
        # localtime = time.localtime(time.time())
        # 格式化成2016-03-20 11:45:39
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return t

    #随机订单id
    @staticmethod
    def radid():
        # base = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        #         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        base='1234567890abcdefghijklmnopqrstuvwxyz'
        numb = "".join(r.sample(base,32))
        # print(numb)
        return numb

    #验签反查MD5加密
    @staticmethod
    def setmd5(jsons):
        # 字典类型dict转json并去掉内部中文转码
        j=json.dumps(jsons, ensure_ascii=False)
        sign = j+ c.parksig
        m = hashlib.md5()
        b = sign.encode(encoding='utf-8')
        m.update(b)
        return m.hexdigest()


    #替换json中的value
    def print_keyvalue_all(input_json):

        if isinstance(input_json, dict):
            for key in input_json.keys():
                key_value = input_json.get(key)
                if isinstance(key_value, dict):
                    print_keyvalue_all(key_value)
                elif isinstance(key_value, list):
                    for json_array in key_value:
                        print_keyvalue_all(json_array)
                else:
                    print(str(key) + " = " + str(key_value))
        elif isinstance(input_json, list):
            for input_json_array in input_json:
                print_keyvalue_all(input_json_array)

