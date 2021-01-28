from flask import Flask
# app = Flask(__name__)
from db_config import app
# 导入user模块
from handler.user import user

# 注册蓝图
app.register_blueprint(user, url_prefix="/user")


# 商品模块
# 订单模块


@app.route('/')
def hello():
    return 'hello'


if __name__ == '__main__':
    app.run()
