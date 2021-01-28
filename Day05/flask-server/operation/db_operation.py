# 引入数据模型
from models.models import User
from db_config import db_init as db

# 数据表操作的类
class User_Operation():
    def __init__(self):
        self.__fields__ = ["id", "username", "password", "phone", "others"]

    def _all_user(self):
        #数据库查询.query.all()
        user_list = User.query.all()
        return user_list

    def _reg(self, kwargs):
        #coding：查询用户名是否重复
        u = User(**kwargs)
        # 增加一条数据记录
        db.session.add(u)
        db.session.commit()
        return "register success"

    def _login(self,username,password):
        #用户名是否存在
        user_data = User.query.filter_by(username=username).first()
        db_pwd = user_data.password
        if db_pwd == password:
            return "success"
        else:
            return "fail"

