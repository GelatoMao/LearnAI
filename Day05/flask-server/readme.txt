# 基于flask框架的后台服务
1、数据库操作
2、数据模型
3、业务逻辑功能函数
4、模块化

准备：
mysql
HSsql/Navictaformysql

pip:
    pymysql
    flask_sqlalchemy


项目结构：
# app.py  程序入口：服务启动，注册蓝图模块
# db_config.py 数据库配置
# handler （蓝图模块：路由配置） user.py  goods.py   
# api       user_api.py 数据接口实现：功能方法
# operation  数据库操作类  db_operation.py  User_operation类
# models     数据模型类   models.py  User类  Goods类 
# utils     工具包  数据格式转换的功能方法


# app启动后台服务
app-->handler-->api--->operation--->models


handler             view
api                 controller
operation--->models model
MVC

