# !/usr/bin/env python
from __future__ import print_function
import time, hashlib,json
import random as r
import string
import pytest_api.comzt.readconfig as r

read=r.readconfig().conf()
parksig=read['cloud']['parksig']


class Publicdef():

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
        base='1234567890abcdefghijklmnopqrstuvwxyz'
        numb = "".join(r.sample(base,32))
        return numb

    #随机产生orderid
    @staticmethod
    def randomoid():
        # 指定随机数长度
        r_num = 32
        orderid = ''.join(r.sample(string.digits + string.ascii_letters,r_num))
        return orderid

    #验签反查MD5加密
    @staticmethod
    def setmd5(jsons):
        # 字典类型dict转json并去掉内部中文转码
        j=json.dumps(jsons, ensure_ascii=False)
        sign = j+parksig
        m = hashlib.md5()
        b = sign.encode(encoding='utf-8')
        m.update(b)
        return m.hexdigest()

# if __name__ == '__main__':
#     p=Publicdef()
