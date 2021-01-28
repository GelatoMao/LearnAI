# WSGI封装了底层的东西 能够拿到用户的请求 对请求进行处理后返回给flask 触发flask的一些api 最后再返回给用户
from flask import Flask
# Flask类的对象实例就是一个WSGI应用程序
app = Flask(__name__)

# 装饰器：url路径，指定处理这个url的函数
@app.route('/')
def hello():
  return 'hello'

if __name__ == '__main__':
  # web应用程序启动
  app.run()

