# !/usr/bin/env python

import json

from kafka import KafkaProducer
from kafka.errors import KafkaError
from common import publicdef as p

producer = KafkaProducer(bootstrap_servers='10.10.203.201:9092,10.10.203.202:9092,10.10.203.203:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
# 获取当前时间
sata = p.publicdef()
iotime = sata.Dat()

# 代扣topic
dk_topic = 'dc.dk.park.out'
# sign
SigTopic = "dc.sign.park.in"

# 捷顺验签数据
js_signjson = {"serviceId": "fc.park.signatoryResult.OrderQuery", "data": {"parkCode": "20181213001", "dataItems": [
    {"carNo": "藏-JK1111", "inTime": "" + iotime + "", "vehicleInfo": "{\"plateColor\":\"BLUE\"}"}]}}

# 捷顺出场代扣数据
js_outjson = {"isReal": 0, "parkName": "梅test1", "ysMoney": 0.01, "overTimeYSMoney": 0, "overTimeHGMoney": 0,
              "yhMoney": 0.01, "inEquipName": "入口_230", "outMode": "HIGHFEE", "outOperator": "用户管理员",
              "outEquipCode": "14", "overTimeSSMoney": 0, "ssMoney": 0.0, "freeMoney": 0, "dkTag": 1,
              "overTimeFlag": 0, "idno": "藏-JK1111", "payTypeName": "CASH", "carNumber": "藏-JK1111",
              "inTime": "" + iotime + "", "itemId": "83d7614331a54b7195a4b96830598fb1", "outEquipName": "出口_230",
              "overTimeYHMoney": 0, "inEquipCode": "13", "parkCode": "20181213001", "hgMoney": 0,
              "outTime": "" + iotime + "", "vehicleInfo": "{\"plateColor\":\"BLUE\"}"}


class kafkatools:
    # 发送出场代扣数据
    def send_out(topic, json_data):
        print('begin')
        try:
            producer.send(topic, json_data)
        except KafkaError as e:
            print(e)
        finally:
            producer.close()
            print('done')

# if __name__ == '__main__':
#     kafkatools.send_out(dk_topic, js_outjson)
