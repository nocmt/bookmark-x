from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt() # 初始化加密模块
db = SQLAlchemy()  # 初始化数据库模块


def create_app():
    """ 创建app的方法 """
    app = Flask(__name__)  # 生成Flask对象
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI  # 配置app的URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)  # SQLAlchemy初始化App
    # 在这还可以设置好配置后， 初始化其他的模块
    bcrypt.init_app(app)  # 加密模块载入
    return app  # 返回Flask对象app
