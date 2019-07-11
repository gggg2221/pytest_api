# !/usr/bin/env python

# 请求服务url
ORDERIP = "10.10.203.19:8081";

SIGNIP = "10.10.203.33:8185";

OldSIGNIP = "10.10.203.33:8085";

ORDER_URL = "http://" + ORDERIP + "/order-api-dispatcher/order/dispatcher";

SIGN_URL = "http://" + SIGNIP + "/jscsp-signatory/serviceRequest/signatory";

OldSIGN_URL = "http://" + OldSIGNIP + "/jscsp-signatory/signatory.servlet";

# 云订单redisIp
redisIP = "10.10.203.12";

# 车场密钥
parksig = "7c44531ec05af74c1bd8df3975e8011e";

# sign
SigTopic = "dc.sign.park.in";

# dktopic
DkTopic = "dc.dk.park.out";
