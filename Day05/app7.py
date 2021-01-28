# 会话：session
from flask import Flask, request, Response, jsonify, session
app = Flask(__name__)

# 1.定义密钥
app.secret_key = '123124'

@app.route('/')
def hello():
  return 'hello'

# 登录：
@app.route('/login',methods = ['GET'])
def login():
  username = request.args.get('username')
  # 2.存储到session
  session['username'] = username
  return "登陆成功"

# 主页
@app.route('/home', methods=['GET'])
def home():
  username = session['username']
  return F"{username}已经登录"



# 主页：


if __name__ == '__main__':
  app.run(debug = True)