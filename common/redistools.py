#!/usr/bin/env python
import time
import random
import json
from redis import StrictRedis

re = StrictRedis(host='10.10.203.12', port=6379, password='Jht123456')

a1=(2018,1,1,0,0,0,0,0,0)       #设置开始日期时间元组（2018-01-01 00：00：00）
a2=(2018,12,31,23,59,59,0,0,0)  #设置结束日期时间元组（2018-12-31 23：59：59）
start1=time.mktime(a1)          #生成开始时间戳
end1=time.mktime(a2)            #生成结束时间戳
corderNos = "ee3b26da3d74476d9ba1eafc260a"
sorderNos = "BK55f22095495744c49d930589d"
cid="692a1b6fe7fa40f0ac88f429fe72"
goodTitle='停车费用-粤-P99900-终端测试0314'
num=0

# SC_JSCSP_ORDER_ORDER_NO_BK55f22095495744c49d930589d_INFO

# 生成渠道验签数据
def channel_sign():
    keyss = 'JSCSP:SIGN:CARSIGNRECORD:CODE.INFO:晋-KV1111'
    k2='8946437fe2824ad5a52509a0ddb967aa'
    dict = {
        "agreementStatus": 0,
        "businesserCode": "",
        "carNumber": "晋-KV1111",
        "channelCode": "CH20180303101443947",
        "channelId": "08e58b78af37404bac12aac12337c109",
        "channelName": "微信车主平台",
        "dkCode": "CCB_SZ",
        "freeTime": "1800",
        "inTime": "2018-11-12 10:35:41",
        "isDirectPushOrder": 0,
        "isUseFund": "0",
        "itemId": "3b923d3fab3e4d96826d017203febc86",
        "openId": "",
        "parkCode": "2018090410",
        "parkName": "2018090410",
        "partnerAccount": "1461511702",
        "partnerAppId": "wx604f61d217d8e0b0",
        "plateColor": "BLUE",
        "serviceKey": "e1436821c8a70c4c7804f72da8dbef45",
        "signKey": "147ba26e2df7b44a8d8a5351bc550a9c",
        "subAppId": "",
        "subMchId": "",
        "url": "http://10.10.29.25:8080/jhtpaydispatch/pay/dispatch",
        "userId": ""
    }

#字典转化字符串

    encode_json = json.dumps(dict)

    re.hmset(keyss,{k2:encode_json})

#生成捷顺验签数据
def js_sign():
    keyss = 'JSCSP:SIGN:CARSIGNRECORD:CODE.INFO:粤-JSJKQB'
    k2 = '29abc3bcb1d34e6bbaa3ce87410a29b1'
    dict = {
        "agreementStatus": 0,
        "carNumber": "粤-JSJKQB",
        "channelName": "一网通",
        "dkCode": "CMB",
        "inTime": "2018-11-07 11:38:53",
        "itemId": "29abc3bcb1d34e6bbaa3ce87410a29b1",
        "parkCode": "2018090410",
        "plateColor": "BLUE",
        "userId": "37bb9853fa904843a2fbd1e0f3c0d27d"
    }

    # 字典转化字符串

    encode_json = json.dumps(dict)

    re.hmset(keyss, {k2: encode_json})

#扫码付-生成订单redis缓存数据
def smzdf(self):

    # keyss='SC_JSCSP_ORDER_ORDER_NO_BK55f22095495744c49d930589d_INFO'
    for num in range(self):
        num = num + 1
        # print(orderNos+str(num))
        ors=sorderNos+str(num)
        ids=cid+str(num)
        # print(ors)
        keyss = 'SC_JSCSP_ORDER_ORDER_NO_' + ors + '_INFO'
        # print(keyss)
        t = random.randint(start1,end1)  # 在开始和结束时间戳中随机取出一个
        date_time = time.localtime(t)    # 将时间戳生成时间元组
        date = time.strftime("%Y-%m-%d %H:%M:%S", date_time)
        # print(date)

        dict = {'otherFree': '0',
                'attentionUrl': '',
                'serviceTime': '779435',
                'couponValue': '',
                'attentionPhoto': '',
                'from': '',
                'isvId': 'PI1516700392902867067',
                'orderType': 'SP',
                'createTime': '2019-05-30 17:18:58',
                'accessSource': 'APP',
                'totalFee': '810',
                'goodTitle': '停车费用-京-E00001-子系统0119',
                'appType':'APP_JSCARLIFE',
                'startTime':date,
                'serviceFee': '',
                'businesserId': 'ff80808155bff34b0155c34f4bab000b',
                'transportFee': '0',
                'merGID': '0324BE8A5D00',
                'businesserName': '顺易通测试商户平台',
                'parkCode':'2018011901',
                'businesserCode':'880085202558012',
                'endTime': '2019-06-08 17:49:33',
                'isShow': '0',
                'joinType': '0',
                'parkInId': '',
                'parkName': '子系统0119',
                'deductFee': '200',
                'userId': '',
                'discountId': '',
                'car_id': '',
                'is_lock': '0',
                'serviceId': 'JSCSP_ORDER_SCANGENERATE',
                'subsystemUrl': 'http://192.168.1.88/JSTPay/',
                'id': ids,
                'couponNo': '',
                'couponType': '',
                'quickExit': '',
                'orderNo': ors,
                'url1631': 'http://192.168.1.88/JSTPay//BookSearch.aspx?gcode_id=2018011901&goods_name=JSPAY&input_charset=GBK&mer_gid=0324BE8A5D00&partner=880085202558012&service_version=1.0&sign_type=MD5&sign=205D9CB27CCB5A703B736ACEF93EFED9',
                'seqId': '',
                'gcodeId': '2018011901',
                'orderStatus': '-1',
                'url': 'http://121.34.253.100:7041/cloud',
                'discountFee': '200',
                'is_map': '0',
                'carNo': '',
                'memberMode': '',
                'subSystemCode': '2018011901',
                'parkId': 'C0F8E13A04944233AEE3040FAE720E25',
                'isStat': '0',
                'attentionRemark': '',
                'validTimeLen': '180'}
        # print(dict)
        re.hmset(keyss, dict)


#车牌主动付-生成订单redis缓存数据
def carzdf():

    for num in range(2):
        num=num+1
        # print(orderNos+str(num))
        ors=corderNos+str(num)
        # print(ors)
        keyss = 'SC_JSCSP_ORDER_ORDER_NO_' + ors + '_INFO'
        # print(keyss)
        dict = {'otherFree': '0',
                'attentionUrl': 'https://www.pgyer.com/JTCTest',
                'serviceTime': '949967',
                'couponValue': '',
                'attentionPhoto': '/parkPic/2017-03-24/160542303_373.png',
                'from': '',
                'isvId': 'PI1510292363953283630',
                'orderType': 'VNP',
                'createTime': '2019-06-11 15:13:31',
                'accessSource': 'APP',
                'totalFee': '1',
                'goodTitle': '停车费用-粤-P99900-终端测试0314',
                'startTime':'2018-05-31 15:20:43',
                'serviceFee': '1',
                'businesserId': 'ff80808155bff34b0155c34f4bab000b',
                'transportFee': '0',
                'merGID': '粤P99900',
                'businesserName': '顺易通测试商户平台',
                'copycarno':'粤P99900',
                'parkCode': 'jsds20170314',
                'businesserCode': '880085202558012',
                'endTime': '2019-06-11 15:13:30',
                'isShow': '0',
                'joinType': '2',
                'parkInId': '',
                'parkName': '终端测试0314',
                'deductFee':'0',
                'userId': '',
                'discountId': '',
                'car_id': '0',
                'is_lock': '0',
                'serviceId': 'JSCSP_ORDER_CARNOGENERATE',
                'subsystemUrl': 'http://#',
                'id': '58ac994eb5244ef987471fbe48696d78',
                'couponNo': '',
                'couponType': '',
                'quickExit': '',
                'orderNo': ors,
                'url1631': 'http://#',
                'seqId': '123456',
                'gcodeId': 'jsds20170314',
                'orderStatus': '-1',
                'url': 'http://121.34.253.100:7041/cloud',
                'discountFee': '0',
                'is_map': '1',
                'carNo': '粤P99900',
                'memberMode': '',
                'subSystemCode': 'jsds20170314',
                'parkId': '0d9aaeeb08a911e7b51a6c3be50c9895',
                'isStat': '0',
                'attentionRemark': '',
                'validTimeLen':'180'}
        # print(dict)
        re.hmset(keyss, dict)


#商户支付方式

def addbuspaytype():
        keyss='SC_JSCSP_ORDER_BUSINESSER_ID_PAYTYPE_APPTYPE_ff80808155bff34b0155c34f4bab000b_CUP_UMS_PUB__PAYTYPE'
        dict = {'priKey': '',
                'appType': '',
                'reqUrl': '',
                'operNo': '',
                'pubKey': '',
                'branchId': '',
                'serviceKey': 'fcAmtnx7MwismjWNhNKdHC44mNXtnEQeJkRrhKJwyrW2ysRR',
                'partnerAccount': '898340149000005',
                'subMchId': '',
                'productCode': '',
                'status': 'NORMAL',
                'partnerAppId': '',
                'signType': 'MD5',
                'operPwd': '',
                'subAppId': '',
                'goodTag': '',
                'payUrl': '',
                'payType': 'CUP_UMS_PUB',
                'businesserId': 'ff80808155bff34b0155c34f4bab000b',
                'posId': '',
                'id': 'ff808x8153352b780153366ba1020004',
                }
        re.hmset(keyss, dict)

#删除扫码付redis订单数据
def delsmkey(self):

    for num in range(self):
        num=num+1
        # print(orderNos+str(num))
        ors=sorderNos+str(num)
        # print(ors)
        keyss = 'SC_JSCSP_ORDER_ORDER_NO_' + ors + '_INFO'
        re.delete(keyss)


#删除主动付redis订单数据
def delcarkey():
    for num in range(2):
        num=num+1
        # print(orderNos+str(num))
        ors=corderNos+str(num)
        # print(ors)
        keyss = 'SC_JSCSP_ORDER_ORDER_NO_' + ors + '_INFO'
        re.delete(keyss)

if __name__== '__main__':
    ()
