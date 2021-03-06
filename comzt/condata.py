# !/usr/bin/env python
import comzt.publicdef as p
import comzt.readconfig as r


read=r.readconfig().read_config()
ORDERIP=read['cloud']['orderip']
NEWSIGNIP=read['cloud']['newsignip']
OldSIGNIP=read['cloud']['oldsignip']
PARKCODE=read['cloud']['parkcode']

HTTP="http://"
ORDER_URL = HTTP + ORDERIP + "/order-api-dispatcher/order/dispatcher"
SIGN_URL = HTTP + NEWSIGNIP + "/jscsp-signatory/serviceRequest/signatory"
OldSIGN_URL = HTTP + OldSIGNIP + "/jscsp-signatory/signatory.servlet"

JSCARNO="藏-JK1111"
ZFBCARNO="藏-ZFB999"
WXCARNO="藏-CS1111"

CARCOLOR="{\"plateColor\":\"BLUE\"}"

# 随机产生orderid
ODERID = p.Publicdef.randomoid()

# 获取当前时间
iotime = p.Publicdef.getdate()

# 捷顺验签反查数据
js_signjson ={"serviceId": "fc.park.signatoryResult.OrderQuery", "data": {"parkCode": "20181213001", "dataItems": [
    {"carNo": JSCARNO, "inTime": "" + iotime + "", "vehicleInfo": CARCOLOR}]}}

# wx验签反查数据
wx_signjson ={"serviceId": "fc.park.signatoryResult.OrderQuery", "data": {"parkCode": "20181213001", "dataItems": [
    {"carNo": WXCARNO, "inTime": "" + iotime + "", "vehicleInfo": CARCOLOR}]}}

# zfb验签反查数据
zfb_signjson ={"serviceId": "fc.park.signatoryResult.OrderQuery", "data": {"parkCode": "20181213001", "dataItems": [
    {"carNo": ZFBCARNO, "inTime": "" + iotime + "", "vehicleInfo": CARCOLOR}]}}

# 捷顺出场代扣数据
js_outjson = {"isReal": 0, "parkName": "梅test1", "ysMoney": 0.01, "overTimeYSMoney": 0, "overTimeHGMoney": 0,
              "yhMoney": 0.01, "inEquipName": "入口_230", "outMode": "HIGHFEE", "outOperator": "用户管理员",
              "outEquipCode": "14", "overTimeSSMoney": 0, "ssMoney": 0.0, "freeMoney": 0, "dkTag": 1,
              "overTimeFlag": 0, "idno": JSCARNO, "payTypeName": "CASH", "carNumber": JSCARNO,
              "inTime": "" + iotime + "", "itemId": "83d7614331a54b7195a4b96830598fb1", "outEquipName": "出口_230",
              "overTimeYHMoney": 0, "inEquipCode": "13", "parkCode": "20181213001", "hgMoney": 0,
              "outTime": "" + iotime + "", "vehicleInfo": CARCOLOR}

#微信代扣出场数据
wxoutjson= {"isReal":0,"parkName":"梅test","ysMoney":0.01,"yhMoney":0.00,"inEquipName":"车场入口","outMode":"NORMAL",
            "outOperator":"Admin","outEquipCode":"2","ssMoney":0.01,"freeMoney":0,"dkTag":1,"orderNo":"",
            "outCarPhoto":"2018113019/NISSP_IMG_PARK_OUT/20181112/1","vehicleInfo":CARCOLOR,"overTimeFlag":0,"idno":"01181016100552",
            "inRecordId":"" + ODERID + "","payTypeName":"线上代扣","carNumber":WXCARNO,"inTime":"" + iotime + "","itemId":"" + ODERID + "" ,"outEquipName":"车场出口",
            "inEquipCode":"6","parkCode":PARKCODE,"hgMoney":0.0,"outTime":"" + iotime + ""}

#支付宝代扣出场数据
zfboutjson= {"isReal":0,"parkName":"梅test","ysMoney":0.01,"yhMoney":0.0,"inEquipName":"车场入口","outMode":"NORMAL","outOperator":"Admin",
"outEquipCode":"2","ssMoney":0.01,"freeMoney":0,"dkTag":1,"orderNo":"","outCarPhoto":"20181213001/NISSP_IMG_PARK_OUT/20181112/1","vehicleInfo":CARCOLOR,
             "overTimeFlag":0,"idno":"01181016100552","inRecordId":"" + ODERID + "","payTypeName":"线上代扣","carNumber":ZFBCARNO,
             "inTime":"" + iotime + "","itemId":"" + ODERID + "","outEquipName":"车场出口","inEquipCode":"6","parkCode":PARKCODE,
             "hgMoney":0.0,"outTime":"" + iotime + ""}

#老验签
zfb_signojson={"total":1,"business_no":"20181213002","dataItems":[{"attributes":{"carno":ZFBCARNO}}],"park_code":"20181213001"}
