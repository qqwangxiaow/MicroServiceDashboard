# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 5/24/19 2:26 AM
from flask import jsonify, request
from app.cache import cache
from app.libs.promise import promise
from app.libs.redprint import Redprint
from app.libs.micro_function import get_config_data as get_config, get_size, get_performance, get_count
from app.libs.token_auth import auth
from app.validators.forms import DataForm, ConfigDataForm
from app.libs.enums import MicroServiceEnum

api = Redprint('data')

@api.route('/config', methods=["GET"])
def get_config_data():
    form = ConfigDataForm().validate_for_api()
    config = get_config(form.microservices.data)
    return jsonify(config)


@api.route('', methods=["GET"])
# @auth.login_required
def get_micro_data():
    form = DataForm().validate_for_api()
    micro = promise[form.microservice.data]()
    return jsonify(micro)


@api.route('/json', methods=["GET"])
@cache.cached(timeout=3600)
# @auth.login_required
def return_json():
    return jsonify(MicroServiceEnum.convert_enum_dict())


@api.route('', methods=['POST'])
def insert_micro_data():
    pass


@api.route('', methods=['DELETE'])
def delete_micro_data():
    pass


@api.route('/size', methods=['GET'])
def get_micro_size():
    form = DataForm().validate_for_api()
    micro_sizes = get_size(form.microservice.data)
    return jsonify(micro_sizes)


@api.route('/size', methods=['DELETE'])
def delete_micro_size():
    pass


@api.route('/performance', methods=['GET'])
def get_micro_performance():
    form = DataForm().validate_for_api()
    micro_sizes = get_performance(form.microservice.data)
    return jsonify(micro_sizes)


@api.route('/performance', methods=['DELETE'])
def delete_micro_performance():
    pass


@api.route('/count', methods=['GET'])
def get_test_count():
    form = DataForm().validate_for_api()
    micro_count = get_count(form.microservice.data)
    return jsonify(micro_count)
