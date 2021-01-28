from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# 数据库配置中必须要有app 所以将app设置在这里 app.py中的app从这边导入
app = Flask(__name__)

# 配置当前服务的数据库参数 //root:密码@ip:port/数据库名
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:mltj2015@127.0.0.1:3306/demo"
# 数据库初始化
db_init = SQLAlchemy(app)