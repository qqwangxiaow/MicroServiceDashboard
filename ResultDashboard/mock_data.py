# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 6/4/19 1:08 AM
from app import create_app
from app.models.base import db
from app.models.data import MicroSizeData, MicroPerformance
import random
from app.validators.forms import StorePerformance
import datetime

app = create_app()
with app.app_context():
    with db.auto_commit():
        for i in range(2000):
            os = random.choice(["CentOS", "ClearLinux", "Ubuntu"])
            v = ["pybenchmark Average"]
            obj = MicroPerformance()
            obj.micro_code = 1001
            obj.OS = os
            obj.runtime = random.choice(['kata', 'runc'])
            obj.machine = 'i9'
            obj.version = "v1.0.{}".format(i)
            obj.catalog = "Language"
            obj.docker_type = random.choice(['Default Docker', 'Clear Docker'])
            obj.kpi = v[0]
            obj.data = i
            obj.publish_date = datetime.datetime.now()
            db.session.add(obj)
