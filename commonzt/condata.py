# !/usr/bin/env python

from commonzt import publicdef as p

# 请求服务url
ORDERIP = "10.10.203.19:8081"

SIGNIP = "10.10.203.33:8185"

OldSIGNIP = "10.10.203.33:8085"

ORDER_URL = "http://" + ORDERIP + "/order-api-dispatcher/order/dispatcher"

SIGN_URL = "http://" + SIGNIP + "/jscsp-signatory/serviceRequest/signatory"

OldSIGN_URL = "http://" + OldSIGNIP + "/jscsp-signatory/signatory.servlet"

# 云订单redisIp
redisIP = "10.10.203.12"

# 车场密钥
parksig = "7c44531ec05af74c1bd8df3975e8011e"

# sign
SigTopic = "dc.sign.park.in"

# dktopic
DkTopic = "dc.dk.park.out"

# 获取当前时间
iotime = p.publicdef().Dat()

# 捷顺验签反查数据
js_signjson ={"serviceId": "fc.park.signatoryResult.OrderQuery", "data": {"parkCode": "20181213001", "dataItems": [
    {"carNo": "藏-JK1111", "inTime": "" + iotime + "", "vehicleInfo": "{\"plateColor\":\"BLUE\"}"}]}}

# 捷顺出场代扣数据
js_outjson = {"isReal": 0, "parkName": "梅test1", "ysMoney": 0.01, "overTimeYSMoney": 0, "overTimeHGMoney": 0,
              "yhMoney": 0.01, "inEquipName": "入口_230", "outMode": "HIGHFEE", "outOperator": "用户管理员",
              "outEquipCode": "14", "overTimeSSMoney": 0, "ssMoney": 0.0, "freeMoney": 0, "dkTag": 1,
              "overTimeFlag": 0, "idno": "藏-JK1111", "payTypeName": "CASH", "carNumber": "藏-JK1111",
              "inTime": "" + iotime + "", "itemId": "83d7614331a54b7195a4b96830598fb1", "outEquipName": "出口_230",
              "overTimeYHMoney": 0, "inEquipCode": "13", "parkCode": "20181213001", "hgMoney": 0,
              "outTime": "" + iotime + "", "vehicleInfo": "{\"plateColor\":\"BLUE\"}"}
#老验签
wx_signojson={"total":1,"business_no":"20181213002","dataItems":[{"attributes":{"carno":"鲁-PPPPP1"}}],"park_code":"20181213001"}