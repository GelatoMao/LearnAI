from flask import Blueprint, request, jsonify
from api.user_api import *

# 创建蓝图
user = Blueprint('user', __name__)


# 用户模块 user/list   user/login   user/register    user/changepwd
# 路由配置
@user.route('/list')
def user_list():
    # 使用用户列表功能
    list = User_List()
    return jsonify(list)


# get 注册 username password phone others
@user.route('/reg', methods=['GET'])
def reg():
    # GET path 参数列表
    username = request.args.get("username")
    password = request.args.get("password")
    phone = request.args.get("phone")
    others = request.args.get("others")
    # 验证
    # 使用户注册功能
    result = User_reg({
        "username": username,
        "password": password,
        "phone": phone,
        "others": others
    })
    return jsonify(result)


# 登录 GET username password
@user.route('/login', methods=['GET'])
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    #验证
    result = User_login(username, password)
    return jsonify(result)