from operation.db_operation import User_Operation
from utils.data_process import *

# 所有用户相关的业务处理函数


# 返回用户列表方法
def User_List():
    # 数据库操作模块 (SQL语句) : 操作类，数据模型类
    u_o = User_Operation()
    result_data = u_o._all_user()
    # 数据库操作的结果，不能直接返回
    # 处理称字典格式
    result = Class_To_Data(result_data, u_o.__fields__)
    return result


# 注册方法
def User_reg(kwargs):
    # coding：业务判断
    u_o = User_Operation()
    result = u_o._reg(kwargs)
    return result


#登录方法
def User_login(username, password):
    u_o = User_Operation()
    result = u_o._login(username, password)
    return result