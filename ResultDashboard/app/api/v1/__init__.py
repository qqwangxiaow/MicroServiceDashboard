# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 5/22/19 11:49 PM

from flask import Blueprint
from app.api.v1 import user, client, token, data


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    data.api.register(bp_v1)
    return bp_v1
