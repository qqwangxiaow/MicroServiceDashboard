# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 6/4/19 1:08 AM
from app import create_app
from app.models.base import db
from app.models.data import MicroSizeData
import random
from app.validators.forms import StorePerformance

app = create_app()
with app.app_context():
    with db.auto_commit():
        for i in range(1000):
            os = ["CentOS", "ClearLinux", "Ubuntu"] * 1000
            type_ = ["Clear Docker", "Default Docker"] * 1000
            v = ["pybenchmark Average", "pybenchmark minimum"] * 1000
            obj = MicroPerformance()
            obj.micro_code = 1001
            obj.OS = os[i]
            # obj.size = float("33.{}".format(i))
            obj.version = "v1.0.{}".format(i)
            obj.catalog = "Language"
            obj.docker_type = type_[i]
            obj.kpi = v[i]
            obj.data = i
            db.session.add(obj)
