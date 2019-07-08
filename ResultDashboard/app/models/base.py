# _*_coding:utf-8_*
# author: XiaHuaLou
# Create Time: 4/25/19 12:00 PM
from datetime import datetime
from contextlib import contextmanager
from sqlalchemy import Column, Integer, SmallInteger
from flask import current_app
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery

from app.libs.error_code import NotFound

__author__ = 'xiahualou'
__all__ = ['db', 'Base']


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self, throw=True):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            current_app.logger.exception('%r' % e)
            if throw:
                raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident, description=None):
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv

    def first_or_404(self, description=None):
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv


db = SQLAlchemy(query_class=Query)


# class BaseMixin(object):
#     def __getitem__(self, key):
#         return getattr(self, key)


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    designer = __author__

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)
        return self

    def append(self, *keys):
        for key in keys:
            self.fields.append(key)
        return self

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


class BaseUser(Base):
    __abstract__ = True
    status = Column(SmallInteger, default=1)

    def delete(self):
        self.status = 0


class BaseNoCreateTime(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)


class BaseData(Base):
    __abstract__ = True
