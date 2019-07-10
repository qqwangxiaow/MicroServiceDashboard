# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 6/4/19 1:08 AM
from app import create_app
from app.models.base import db
from app.models.data import MicroSizeData
import random

app = create_app()
with app.app_context():
    with db.auto_commit():
        for i in range(100):
            obj = MicroSizeData()
            obj.micro_code = 1001
            obj.OS = "ClearLinux"
            obj.size = float("33.{}".format(i))
            obj.version = "v1.0.{}".format(i)
            obj.catalog = "Language"
            obj.docker_type = "Default Docker"
            db.session.add(obj)
