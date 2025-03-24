from flask import Flask, jsonify
from common.mysql_operate import db

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonify返回的中文正常显示

data = [
    {"id": 1, "username": "小明", "password": "123456", "role": 0, "sex": 0, "telephone": "10086", "address": "北京市海淀区"},
    {"id": 2, "username": "李华", "password": "abc", "role": 1, "sex": 0, "telephone": "10010", "address": "广州市天河区"},
    {"id": 3, "username": "大白", "password": "666666", "role": 0, "sex": 1, "telephone": "10000", "address": "深圳市南山区"}
]


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/users", methods=["GET"])
def get_all_users():
    """获取所有用户信息"""
    sql = "SELECT * FROM user"
    data = db.select_db(sql)
    print("获取所有用户信息 == >> {}".format(data))
    return jsonify({"code": 0, "data": data, "msg": "查询成功"})



@app.route("/users/<string:username>", methods=["GET"])
def get_user(username):
    """获取某个用户信息"""
    sql = "SELECT * FROM user WHERE username = '{}'".format(username)
    data = db.select_db(sql)
    print("获取 {} 用户信息 == >> {}".format(username, data))
    if data:
        return jsonify({"code": 0, "data": data, "msg": "查询成功"})
    return jsonify({"code": "1004", "msg": "查不到相关用户的信息"})



if __name__ == '__main__':
    app.run()

