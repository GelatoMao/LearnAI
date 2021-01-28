from flask import Flask
# 创建Flask对象 参数和默认值
# __name__
# static_folder="static" 静态资源路径
# template_folder="templates" 模板路径
# root_path
app = Flask(__name__)
@app.route('/')
def hello():
  return 'hello world'

if __name__ == '__main__':
  # 启动web serve
  # app.run(ip(host), 端口, 是否调试)
  app.run(host = '127.0.0.1', port = '5001', debug = True)

