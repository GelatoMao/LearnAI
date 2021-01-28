# 路由配置
# 路由：web应用一般使用语义化的url
# @app.route()绑定path（url）以及处理函数
from flask import Flask

app = Flask(__name__)

# 127.0.0.1:5000/
@app.route('/')
def hello():
  return 'hello world'

# 127.0.0.1:5000/user
@app.route('/user')
def user():
  return '用户信息'

# 路由：字符串参数
@app.route('/username/<username>')
def username(username):
  # 根据username 进行业务处理 返回处理后的值
  return username

# 路由：整型参数
@app.route('/userid/<int:id>')
def userid(id):
  # 返回类型必须是字符串 字典 元祖等信息 
  return F"用户id是{id}"

# 路由：路径参数(path字符串可以包含/)
@app.route('/userinfo/<path:path>')
def userinfo(path):
  return path

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port = '5001', debug = True)

