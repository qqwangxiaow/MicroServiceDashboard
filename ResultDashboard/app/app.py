# _*_coding:utf-8_*
# author: XiaHuaLou
# Create Time: 4/24/19 12:00 PM
from datetime import date
from flask.json import JSONEncoder as _JSONEncoder
from flask import Flask as _Flask

from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    '''rewrite default for serialize object default is a recursion function,if object has attribute cannot be serialize,
    it will send this attribute to default example,user = {"name":"Jerry","time":datetime.date(2019, 5, 21)},cause date
    cannot be serialized,so it will be executed twice,at first time o is user object,at second time,o is user['time']
    '''

    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
