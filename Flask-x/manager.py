from flask_script import Manager

from app import create_app
from app.api import api

app = create_app()  # 创建app
app.register_blueprint(api, url_prefix='/api')  # 注册蓝图


manager = Manager(app)  # 通过app创建manager对象


if __name__ == '__mian__':
    manager.run()  # 运行服务器
