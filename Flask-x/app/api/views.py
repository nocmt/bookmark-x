# 获取蓝图
from app.api import api

# 获取数据库模型对象和SQLAlchemy对象db，注意不可使用App模块中的db
from app.api.models import *
from flask import request
from flask_restful import Api as rApi
from flask_restful import Resource

bookmark_dict = {}

rapi = rApi(api)


# 书签
class bookmark(Resource):
    def get(self):
        bookmark_dict['sort_name'] = request.values.get('sort_name', '')
        return {'s': bookmark_dict['sort_name']}

    def post(self):
        bookmark_dict['link'] = request.form['link']
        return {'link': bookmark_dict['link']}





rapi.add_resource(bookmark, '/bookmark')
