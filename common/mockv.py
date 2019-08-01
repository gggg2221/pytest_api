#!/usr/bin/env python
from flask import Flask,Response
import json

app = Flask(__name__)

@app.route('/test/',methods =['POST','GET'])
def hello_world():
    p1="18022233311"
    p2="18813574284"
    res = {
        "resultCode": "0",
        "message": "success",
        "obj": {
            "phone": p1,
            "name": "杨伟"
        }
    }
    s=Response(json.dumps(res,ensure_ascii=False).encode('utf-8'), content_type='application/json')
    return s

if __name__ == '__main__':
    app.run(host='10.101.90.228',port=5000,debug=True)
