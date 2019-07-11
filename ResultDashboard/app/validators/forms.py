# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 5/23/19 12:48 AM

from wtforms import StringField, IntegerField, FieldList, Field
from wtforms.validators import DataRequired, Length, Email, Regexp, length, ValidationError
from app.libs.enums import ClientTypeEnum, MicroServiceEnum
from app.models import User
from app.validators.base import BaseForm
from app.libs.error_code import MicroServiceNotFoundError


class ListField(Field):
    def __init__(self, label='', validators=None, **kwargs):
        super(ListField, self).__init__(label, validators, **kwargs)

    def process_formdata(self, valuelist):
        try:
            if valuelist[0] and isinstance(valuelist[0], list):
                self.data = valuelist[0]
            else:
                raise ValidationError('list validate error')
        except:
            raise ValidationError('list validate error, exception')


class ClientForm(BaseForm):
    account = StringField(validators=[DataRequired(message='can\'t be null'), Length(min=5, max=32)])
    secret = StringField(validators=[DataRequired(), ])
    nickname = StringField()
    type = IntegerField(validators=[DataRequired(), ])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()


class DataForm(BaseForm):
    microservice = IntegerField(validators=[DataRequired(message='can\'t be null')])
    def validate_microservice(self, value):
        try:
            if value.data.endswith("0000"):
                code = [MicroServiceEnum(int(v)) for v in value.data.split("0000")[:-1]]
            else:
                code = MicroServiceEnum(int(value.data))
        except Exception as e:
            raise MicroServiceNotFoundError(str(e))
        self.microservice.data = code

class PerformanceForm(BaseForm):
    microservice = IntegerField(validators=[DataRequired(message='can\'t be null')])
    kpi = StringField()
    def validate_microservice(self, value):
        self.microservice.data = value.data

    def validate_kpi(self,value):
        self.kpi.data = value.data




class ConfigDataForm(BaseForm):
    microservices = ListField()

    def validate_microservices(self, value):
        return IndentationError()
