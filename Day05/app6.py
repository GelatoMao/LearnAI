# Response响应
from flask import Flask, request, Response, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
  return 'hello'

@app.route('/list', methods=['GET'])
def friendlist():
  list = [
    {"id": 1, "name": "小明"},
    {"id": 2, "name": "小话"},
    {"id": 3, "name": "小画"},
    {"id": 4, "name": "小化"},
    {"id": 5, "name": "小花"}
  ]
  # 接口文档的标准形式
  # 响应状态status: 200ok 500 404
  # 业务状态code:0 正常 -1参数问题 code为0时 list里面才有数据 如果code等于-1 则代表请求失败
  res = {
    "code": 0,
    "data": list
  }
  # jsonify来处理格式
  return jsonify(res)

if __name__ == '__main__':
  app.run(debug = True)