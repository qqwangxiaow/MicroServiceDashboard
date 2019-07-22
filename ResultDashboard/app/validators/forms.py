# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 5/23/19 12:48 AM

from wtforms import StringField, IntegerField, FieldList, Field, DateTimeField, FloatField
from wtforms.validators import DataRequired, Length, Email, Regexp, length, ValidationError
from app.libs.enums import ClientTypeEnum, MicroServiceEnum
from app.models import User, MicroPerformance
from app.validators.base import BaseForm
from app.libs.error_code import MicroServiceNotFoundError, ServerError
import datetime


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

    def validate_kpi(self, value):
        self.kpi.data = value.data


class StorePerformance(BaseForm):
    __column__ = ('publish_date', 'catalog', 'version', 'micro_code',
                  'docker_type', 'data', 'kpi', 'OS', 'machine', 'runtime'
                  )
    docker_type = StringField(validators=[DataRequired(message='can\'t be null')])
    micro_code = IntegerField(validators=[DataRequired(message='can\'t be null')])

    version = StringField(validators=[DataRequired(message='can\'t be null')])
    catalog = StringField(validators=[DataRequired(message='can\'t be null')])
    OS = StringField(validators=[DataRequired(message='can\'t be null')])
    publish_date = DateTimeField(default=datetime.datetime.now())
    data = FloatField(validators=[DataRequired(message='can\'t be null')])
    kpi = StringField(validators=[DataRequired(message='can\'t be null')])
    machine = StringField(validators=[DataRequired(message='can\'t be null')])
    runtime = StringField(validators=[DataRequired(message='can\'t be null')])

    def validate_docker_type(self, value):
        if not value.data in ['Clear Docker', 'Default Docker']:
            raise ServerError('runtime must be "Clear Docker" or "Default Docker"')
        self.docker_type.data = value.data

    def validate_micro_code(self, value):
        self.micro_code.data = value.data

    def validate_version(self, value):
        self.version.data = value.data

    def validate_catalog(self, value):
        self.catalog.data = value.data

    def validate_OS(self, value):
        if not value.data in ['CentOS', 'ClearLinux', 'Ubuntu']:
            raise ServerError('runtime must be "CentOS","ClearLinux" or "Ubuntu"')
        self.OS.data = value.data

    def validate_publish_date(self, value):
        self.publish_date.data = value.data

    def validate_data(self, value):
        self.data.data = value.data

    def validate_kpi(self, value):
        self.kpi.data = value.data

    def validate_machine(self, value):
        self.machine.data = value.data

    def validate_runtime(self, value):
        if not value.data in ['runc', 'kata']:
            raise ServerError('runtime must be "runc" or "kata"')
        self.runtime.data = value.data

    def to_dict(self):
        return self.__column__


class ConfigDataForm(BaseForm):
    microservices = ListField()

    def validate_microservices(self, value):
        return IndentationError()
