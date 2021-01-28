from flask import Flask, render_template
# static templates
app = Flask(__name__)


@app.route('/')
def hello():
  return 'hello'

# 使用静态资源/模板
@app.route('/login')
def login():
  username = "xiaoming"
  pwd = "1234"
  # 返回模板 render_template()渲染复杂内容 使用jinja2模板 可以传递参数 参数在html页面中以双括号形式引入
  return render_template('login.html', username = username, pwd = pwd)

if __name__ == '__main__':
  app.run(debug = True)
