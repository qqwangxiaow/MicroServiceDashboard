# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 5/23/19 12:44 AM
from enum import Enum
from functools import partial

repository = __import__("app.libs.enum_repository", fromlist=True)


def gc(micro):
    return partial(getattr, repository)(micro)


class BaseEnum(Enum):

    @classmethod
    def convert_enum_dict(cls):
        _maps = zip(cls.__dict__["_member_names_"], )
        return {dt[0]: getattr(repository, dt[0]) for dt in _maps}


class ClientTypeEnum(BaseEnum):
    USER_EMAIL = gc("EMAIL")
    USER_ACCOUNT = gc("ACCOUNT")


class MicroServiceEnum(BaseEnum):
    HTTPD = gc("HTTPD")
    PYTHON = gc("PYTHON")
    JENKINS = gc("JENKINS")
    JAVA = gc("JAVA")
    GO = gc("GO")
    MYSQL = gc("MYSQL")
    PHP = gc("PHP")
    NGINX = gc("NGINX")
    POSTGREL = gc("POSTGREL")
    RUBY = gc("RUBY")


