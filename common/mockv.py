#!/usr/bin/env python
from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/test', methods=['POST', 'GET'])
def hello_world():
    p1 = "13111222222"
    p2 = "18813574284"
    res = {
        "resultCode": "0",
        "message": "success",
        "obj": {
            "phone": p1,
            "name": "伟1q"
        }
    }
    s = Response(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type='application/json')
    return s


@app.route('/open/sso/verify_token', methods=['POST', 'GET'])
def app_lg():
    res = {
        "code": "A00000",
        "msg": "",
        "message": "",
        "err_code": "",
        "err_msg": "",
        "isok": True,
        "data": [{
            "name": "系统管理员",
            "loginName": "admin",
            "sex": "",
            "age": "",
            "height": "",
            "mobilePhone": "13512341234"
        }]
    }
    a = Response(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type='application/json')
    return a


if __name__ == '__main__':
    app.run(host='10.101.90.228', port=5000, debug=True)
