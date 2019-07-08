# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 5/24/19 1:01 AM


class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))
        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))
        return self


class AdminScope(Scope):
    forbidden = ['v1.super_delete_user']

    def __init__(self):
        self + UserScope()


class UserScope(Scope):
    allow_module = ['v1.user']
    forbidden = ['v1.super_get_user', 'v1.super_delete_user']


class SuperScope(Scope):
    def __init__(self):
        self + AdminScope()


def is_in_scope(scope, endpoint):
    '''globals() is current module var'''
    scope = globals()[scope]()
    splits = endpoint.split("+")
    request_module = splits[0]
    request_api = '.'.join((endpoint.split('.')[0], splits[-1]))
    if request_api in scope.forbidden:
        return False
    if request_api in scope.allow_api:
        return True
    if request_module in scope.allow_module:
        return True
    else:
        return False
