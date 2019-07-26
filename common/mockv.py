#!/usr/bin/env python
from flask import Flask
import json

app = Flask(__name__)


@app.route('/test/',methods =['POST','GET'])
def hello_world():
    res = {
        "resultCode": "0",
        "message": "success",
        "obj": {
            "telephone": "18813574284",
            "name": "法师"
        }
    }
    return json.dumps(res, ensure_ascii=False).encode('utf-8')

if __name__ == '__main__':
    app.run(host='10.101.90.228',port=5000,debug=True)
