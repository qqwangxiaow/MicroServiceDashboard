# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 5/23/19 4:00 AM
from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 201
    msg = 'sorry,we made a mistake *_*！'
    error_code = 999


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found 0_0...'
    error_code = 1001


class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden,not in scope'


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006
    description = (
        'client is valid'
    )


class MicroServiceNotFoundError(APIException):
    code = 404
    msg = 'MicroService does not exist'
    error_code = 1007

