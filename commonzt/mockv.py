#!/usr/bin/env python
from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/apitest/', methods=['POST', 'GET'])
def hello_world():
    p1 = "13111222222"
    p2 = "18566653995"
    res = {
        "resultCode": "0",
        "message": "success",
        "obj": {
            "phone": p2,
            "name": "钟世梁"
        }
    }
    s = Response(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type='application/json')
    return s


@app.route('/h5Server/v1/User/getUserMobilePhone', methods=['POST', 'GET'])
def app_lg():
    res = {
        "resultCode": "0",
        "message": "success",
        "obj": {
            "phone": "13488861339",
            "name": "赵甜"
        }
    }
    a = Response(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type='application/json')
    return a


if __name__ == '__main__':
    app.run(host='10.101.90.228', port=5000, debug=True)
