from datetime import datetime

from app import db, bcrypt

# ROLE_USER = 0
# ROLE_ADMIN = 1

'''
    Integer	int	普通整数，32位
    Float	float	浮点数
    String	str	变长字符串
    Text	str	变长字符串，对较长字符串做了优化
    Boolean	bool	布尔值
    PickleType	任何python对象	自动使用Pickle序列化
    ---
    primarykey	如果设为True，表示主键
    unique	如果设为True，这列不重复
    index	如果设为True，创建索引，提升查询效率
    nullable	如果设为True，允许空值
    default	为这列定义默认值
'''


# 用户
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String())
    time = db.Column(db.Date, default=datetime.now)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    # role = db.Column(db.SmallInteger, default=ROLE_USER)

    def __repr__(self):
        return f'<User {self.username}>'


# 分类
class Sort(db.Model):
    __tablename__ = 'sort'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(50), index=True)
    time = db.Column(db.Date, default=datetime.now)

    def __repr__(self):
        return f'<Sort {self.name}>'


# 书签
class Bookmark(db.Model):
    __tablename__ = 'bookmark'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(50), index=True)
    url = db.Column(db.String(500))
    img_url = db.Column(db.String(500), nullable=False)
    time = db.Column(db.Date, default=datetime.now)
    sort_id = db.Column(db.Integer, db.ForeignKey('sort.id'))
    sort = db.relationship('Sort', backref=db.backref('articles'))
    exist = db.Column(db.Boolean, default=True, index=True)

    def __repr__(self):
        return f'<Bookmark {self.name}>'
