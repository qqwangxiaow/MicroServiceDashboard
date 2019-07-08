# _*_coding:utf-8_*
# author: XiaHuaLou
# Create Time: 4/24/19 11:05 PM
import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app.libs.error_code import NotFound, AuthFailed
from .base import BaseUser, db
from sqlalchemy import Column, String, Integer, SmallInteger, orm
from app import login_manager

__author__ = "XiaHuaLou"


class User(UserMixin, BaseUser):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String(50), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    auth = Column(SmallInteger, default=1)
    time = datetime.datetime.now()
    __password = Column('password', String(128), nullable=False)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'email', 'user', 'auth', 'time']

    def keys(self):
        return self.fields

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, raw):
        self.__password = generate_password_hash(raw)

    def check_password(self, raw):
        if not self.__password:
            return False
        return check_password_hash(self.__password, raw)

    @staticmethod
    def register_by_email(account, secret, nickname):
        with db.auto_commit():
            user = User()
            user.user = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            raise NotFound(msg='user not found')
        if not user.check_password(password):
            return AuthFailed()
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {
            'uid': user.id,
            'scope': scope,
        }

    @login_manager.user_loader
    def get_user(uid):
        return User.query.get(int(uid))
