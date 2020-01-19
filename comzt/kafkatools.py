# !/usr/bin/env python

import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers='10.10.203.201:9092,10.10.203.202:9092,10.10.203.203:9092',
                         value_serializer=lambda v: json.dumps(v,ensure_ascii=False).encode('utf-8'))

topic=['dc.dk.park.out','dc.sign.park.in']

wxsign='{"total":1,"business_no":"20181213002","dataItems":[{"attributes":{"carno":"藏-ZZ1111"}}],"park_code":"20181213001"}'

class Kafkatools:
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

