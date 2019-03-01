from flask_script import Manager
from app import create_app
from app.api import api
from flask_migrate import Migrate, MigrateCommand
from app.api.models import *


app = create_app()  # 创建app
app.register_blueprint(api, url_prefix='/api')  # 注册蓝图
migrate = Migrate(app, db)

manager = Manager(app)  # 通过app创建manager对象
manager.add_command('db', MigrateCommand)


if __name__ == '__mian__':
    manager.run()  # 运行服务器
