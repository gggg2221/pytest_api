# !/usr/bin/env python

import time, hashlib,json
import random as r
from commonzt import condata as c

class publicdef:

    #获取当前时间
    def Dat(self):
        # 获取当前时间
        # localtime = time.localtime(time.time())
        # 格式化成2016-03-20 11:45:39
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return t

    #随机订单id
    def Randoms(self):
        base = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        base1='1234567890abcdefghijklmnopqrstuvwxyz'
        numb = "".join(r.sample(base1,32))
        # print(numb)
        return numb

    #验签反查MD5加密
    def setMd5(self,jsons):
        # js_signjson = {"serviceId": "fc.park.signatoryResult.OrderQuery","data": {"parkCode": "20181213001", "dataItems": [{"carNo": "藏-JK1111", "inTime": "2019-7-16 10:07:08","vehicleInfo": "{\"plateColor\":\"BLUE\"}"}]}}
        # 字典类型dict转json并去掉内部中文转码
        j=json.dumps(jsons, ensure_ascii=False)
        sign = j+ c.parksig
        # print(sign)
        b = bytes('{}'.format(sign),'utf-8')
        m2 = hashlib.md5(b)
        # print(m2.hexdigest())
        return m2.hexdigest()


# if __name__ == '__main__':
#     #初始化class
#     p = publicdef()
#     print(p.Dat())