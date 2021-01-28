from db_config import db_init as db

# 用户模型
# 数据模型类
class User(db.Model):
    #数据库 数据表的名字
    __tablename__ = 'user'
    # 多个字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=True)
    others = db.Column(db.String(255), nullable=True)

    def __repr__(self):
      # 打印对象：名字
      return '<User %s>' % self.username
