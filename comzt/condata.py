# !/usr/bin/env python

from comzt import publicdef as p

# 请求服务url
ORDERIP = "10.10.203.19:8081"

NEWSIGNIP = "10.10.203.33:8185"

OldSIGNIP = "10.10.203.33:8085"

HTTP="http://"

ORDER_URL = HTTP + ORDERIP + "/order-api-dispatcher/order/dispatcher"

SIGN_URL = HTTP + NEWSIGNIP + "/jscsp-signatory/serviceRequest/signatory"

OldSIGN_URL = HTTP + OldSIGNIP + "/jscsp-signatory/signatory.servlet"

# 云订单redisIp
redisIP = "10.10.203.12"

# 车场密钥
parksig = "e0c8223b7ca64fa5bf4c0e2f97fd8811"

# sign
SigTopic = "dc.sign.park.in"

# dktopic
DkTopic = "dc.order.park.out"

JSCARNO="藏-JK1111"
ZFBCARNO="藏-WW1111"

CARCOLOR="{\"plateColor\":\"BLUE\"}"

# 获取当前时间
iotime = p.Publicdef.getdate()

# 捷顺验签反查数据
js_signjson ={"serviceId": "fc.park.signatoryResult.OrderQuery", "data": {"parkCode": "20181213001", "dataItems": [
    {"carNo": JSCARNO, "inTime": "" + iotime + "", "vehicleInfo": CARCOLOR}]}}



# 捷顺出场代扣数据
js_outjson = {"isReal": 0, "parkName": "梅test1", "ysMoney": 0.01, "overTimeYSMoney": 0, "overTimeHGMoney": 0,
              "yhMoney": 0.01, "inEquipName": "入口_230", "outMode": "HIGHFEE", "outOperator": "用户管理员",
              "outEquipCode": "14", "overTimeSSMoney": 0, "ssMoney": 0.0, "freeMoney": 0, "dkTag": 1,
              "overTimeFlag": 0, "idno": JSCARNO, "payTypeName": "CASH", "carNumber": JSCARNO,
              "inTime": "" + iotime + "", "itemId": "83d7614331a54b7195a4b96830598fb1", "outEquipName": "出口_230",
              "overTimeYHMoney": 0, "inEquipCode": "13", "parkCode": "20181213001", "hgMoney": 0,
              "outTime": "" + iotime + "", "vehicleInfo": CARCOLOR}
#老验签
zfb_signojson={"total":1,"business_no":"20181213002","dataItems":[{"attributes":{"carno":ZFBCARNO}}],"park_code":"20181213001"}
