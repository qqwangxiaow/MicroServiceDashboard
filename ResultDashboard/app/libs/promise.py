# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 5/29/19 4:56 AM
from app.libs.enums import MicroServiceEnum
from app.libs.micro_function import *

promise = {
    MicroServiceEnum.HTTPD: get_httpd,
    MicroServiceEnum.PYTHON: get_python,
}
