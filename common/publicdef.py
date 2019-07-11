# !/usr/bin/env python

import time
import random as r


class publicdef:
    #获取当前时间
    def Dat(self):
        # 获取当前时间
        localtime = time.localtime(time.time())
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



# if __name__ == '__main__':
#     #     #初始化class
#     p = DataTimes()
#     p.Randoms()