# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 5/23/19 4:27 AM
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=False)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate(self):
        pass

    def validate_for_api(self):
        """diy error type"""
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
