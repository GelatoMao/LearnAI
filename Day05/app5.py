# HTTP GET POST
from flask import Flask, request
app = Flask(__name__)

# 路由规则:path，默认是GET
@app.route('/')
def hello():
  return "hello"

# 登录：GET ip+path?username=xiaoming&pwd=123
@app.route('/login', methods=['GET'])
def login():
  # request请求的封装
  # request.method 查看请求方式
  # request.args 查看请求的查询数据
  # request.args.get("key")
  print(request) # <Request 'http://127.0.0.1:5000/login' [GET]>
  print(request.method) # ImmutableMultiDict([('username', 'xiaoming'), ('pwd', '123')])
  print(request.args) 
  print(request.args.get('username')) # xiaoming
  print(request.args.get('pwd')) # 123
  return request.args.get('username')


# 注册：POST 表单 username:xiaoming pwd:123
@app.route('/reg',methods=['POST'])
def reg():
  # request.form 查看请求的查询数据
  print(request.form) # ImmutableMultiDict([('username', 'xiaoming'), ('pwd', '123')])
  print(request.data) # 127.0.0.1 - - [28/Jan/2021 12:51:16] "POST /reg HTTP/1.1" 200 
  return 'hello'

# 文件上传
@app.route('/upload',methods=['POST'])
def upload_img():
  img = request.files['img']
  img.save('img.png')
  return "上传成功"

if __name__ == '__main__':
  app.run(debug = True)