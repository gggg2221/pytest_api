# !/usr/bin/env python

import json,time


from comzt import readconfig as rc
from kafka import KafkaProducer
from kafka.errors import kafka_errors

read=rc.readconfig().read_config()
kafkaip=read['cloud']['kafkaip']

producer = KafkaProducer(bootstrap_servers=kafkaip,
                         value_serializer=lambda v: json.dumps(v,ensure_ascii=False).encode('utf-8'))

# topic=['dc.order.park.out','dc.sign.park.in']

# wxsign='{"total":1,"business_no":"20181213002","dataItems":[{"attributes":{"carno":"藏-ZZ1111"}}],"park_code":"20181213001"}'

class Kafkatools():
    # 发送出场代扣数据
    def send_out(self,topic,json_data):
        try:
            producer.send(topic,json_data)
            time.sleep(0.001)
        except kafka_errors as e:
            print(e)
        finally:
            producer.close()



if __name__ == '__main__':

    for num in range(1,2):
        orderNo = "meitest3d38481743ed9c2b"
        order = orderNo + str(num)
        orderPayId = "meitest3d38481743ed9c2c"
        payid = orderPayId + str(num)
        jsonsync = "{\"cousumerThreadName\":\"\",\"failTime\":\"\",\"from\":\"\",\"orderMainDTO\":null,\"seqId\":\"\",\"serviceId\":\"\",\"syncKafkaDTO\":{\"businesserCode\":\"20181213002\",\"orderCouponId\":\"\",\"orderNo\":\"" + order + "\",\"orderPayId\":\"" + payid + "\",\"partitionKey\":\"1\",\"refundNo\":\"\"}}"
        # producer.send('jscsp.dd4Sjtb.sync',jsonsync)
        producer.send('dc.dk.park.out',jsonsync)
        time.sleep(0.001)

