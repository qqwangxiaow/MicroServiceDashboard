# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 5/29/19 9:34 PM
from app.libs.error_code import MicroServiceNotFoundError, ServerError
from app.models.data import MicroSizeData, MicroPerformance
from app.libs.enums import MicroServiceEnum
from flask import current_app as app
from app.models import db
import app.libs.kpi as KPI
import pandas as pd


def get_config_data(microArray):
    data = {
        "columns": [{"title": "OS"}, {"title": "Processor"}, {"title": "Core"}, {"title": "Threads"},
                    {"title": "InstructionsSet"}, {"title": "Memory"}, {"title": "Storage"}, {"title": "Network"}],
        "rows": [["ClearLinux", 1, 4, 16, 2, "16GB", "2TB", "None"], ]
    }
    return data


def get_count(micro_code):
    return {
        'passed': [250, 310, 320, 340, 400, 500],
        'failed': [65, 120, 130, 50, 40, 60]
    }


def get_size(micro_code):
    try:
        micro = MicroServiceEnum(micro_code).name
        micro_size = MicroSizeData.query.filter(micro_code == micro_code).all()
    except Exception as e:
        raise ServerError(e)
    else:
        size_df = pd.DataFrame([micro.to_dict() for micro in micro_size])
        size_df['MicroService'] = micro
        clear = size_df[size_df['OS'] == 'ClearLinux']
        Ubuntu = size_df[size_df['OS'] == 'Ubuntu']
        CentOS = size_df[size_df['OS'] == 'CentOS']
        default_clear = \
            clear[clear['docker_type'] == 'Default Docker'].sort_values('publish_date', ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'size'].tolist()
        default_ubnutu = \
            Ubuntu[Ubuntu['docker_type'] == 'Default Docker'].sort_values('publish_date', ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'size'].tolist()
        default_centos = \
            CentOS[CentOS['docker_type'] == 'Default Docker'].sort_values('publish_date', ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'size'].tolist()
        clear_clear = \
            clear[clear['docker_type'] == 'Clear Docker'].sort_values('publish_date', ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'size'].tolist()
        clear_ubnutu = \
            Ubuntu[Ubuntu['docker_type'] == 'Clear Docker'].sort_values('publish_date', ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'size'].tolist()
        clear_centos = \
            CentOS[CentOS['docker_type'] == 'Clear Docker'].sort_values('publish_date', ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'size'].tolist()

        columns = [
            {'title': 'DockerType'},
            {"title": 'MicroService'},
            {"title": "Catalog"},
            {"title": "Size(MB)"},
            {"title": "PublishDate"},
            {"title": "Version"},
        ]
        rows = [[*(list(row))] for _, row in
                size_df[['docker_type', 'MicroService', 'catalog', 'size', 'publish_date', 'version']].iterrows()]
        data = {
            "sizeData": [default_clear, default_ubnutu, default_centos, clear_clear, clear_ubnutu, clear_centos],
            "columns": columns,
            "rows": rows,
            "round": list(range(1, app.config['SIZE_ROUND'] + 1)),
            "kpis": getattr(KPI, micro),
            "micro": micro,
        }
    return data


def get_performance(micro_code, kpi, machine='i9'):
    try:
        micro = MicroServiceEnum(int(micro_code)).name
        kpi_define = getattr(KPI, micro)
        if kpi == "default":
            kpi = list(kpi_define.keys())[0]
        units = kpi_define[kpi]
        filters = {
            MicroPerformance.micro_code == micro_code,
            MicroPerformance.kpi == kpi,
            MicroPerformance.machine == machine,
        }
        micros = MicroPerformance.query.filter(*filters).all()
    except Exception as e:
        raise ServerError(e)
    else:
        performance_df = pd.DataFrame([micro.to_dict() for micro in micros])
        performance_df['MicroService'] = micro
        clear = performance_df[performance_df['OS'] == 'ClearLinux']
        Ubuntu = performance_df[performance_df['OS'] == 'Ubuntu']
        CentOS = performance_df[performance_df['OS'] == 'CentOS']
        ClearLinuxDefaultRunc = \
            clear[(clear['docker_type'] == 'Default Docker') & (clear['runtime'] == 'runc')].sort_values('publish_date',
                                                                                                         ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'data'].tolist()
        ClearLinuxDefaultKata = \
            clear[(clear['docker_type'] == 'Default Docker') & (clear['runtime'] == 'kata')].sort_values('publish_date',
                                                                                                         ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'data'].tolist()
        ClearLinuxClearRunc = \
            clear[(clear['docker_type'] == 'Clear Docker') & (clear['runtime'] == 'runc')].sort_values('publish_date',
                                                                                                       ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'data'].tolist()
        ClearLinuxClearKata = \
            clear[(clear['docker_type'] == 'Clear Docker') & (clear['runtime'] == 'kata')].sort_values('publish_date',
                                                                                                       ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'data'].tolist()
        UbuntuDefaultRunc = \
            Ubuntu[(Ubuntu['docker_type'] == 'Default Docker') & (Ubuntu['runtime'] == 'runc')].sort_values(
                'publish_date', ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'data'].tolist()
        print(UbuntuDefaultRunc)
        UbuntuDefaultKata = \
            Ubuntu[(Ubuntu['docker_type'] == 'Default Docker') & (Ubuntu['runtime'] == 'kata')].sort_values(
                'publish_date', ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'data'].tolist()
        UbuntuClearRunc = \
            Ubuntu[(Ubuntu['docker_type'] == 'Clear Docker') & (Ubuntu['runtime'] == 'runc')].sort_values(
                'publish_date', ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'data'].tolist()
        UbuntuClearKata = \
            Ubuntu[(Ubuntu['docker_type'] == 'Clear Docker') & (Ubuntu['runtime'] == 'kata')].sort_values(
                'publish_date', ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'data'].tolist()
        CentOSDefaultRunc = \
            CentOS[(CentOS['docker_type'] == 'Default Docker') & (CentOS['runtime'] == 'runc')].sort_values(
                'publish_date', ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'data'].tolist()
        CentOSDefaultKata = \
            CentOS[(CentOS['docker_type'] == 'Default Docker') & (CentOS['runtime'] == 'kata')].sort_values(
                'publish_date', ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'data'].tolist()
        CentOSClearRunc = \
            CentOS[(CentOS['docker_type'] == 'Clear Docker') & (CentOS['runtime'] == 'runc')].sort_values(
                'publish_date', ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'data'].tolist()
        CentOSClearKata = \
            CentOS[(CentOS['docker_type'] == 'Clear Docker') & (CentOS['runtime'] == 'kata')].sort_values(
                'publish_date', ascending=False).iloc[
            0:app.config['SIZE_ROUND']][
                'data'].tolist()
        columns = [
            {'title': 'DockerType'},
            {"title": 'MicroService'},
            {"title": "Catalog"},
            {"title": '{}({})'.format(kpi, units)},
            {"title": "PublishDate"},
            {"title": "Version"},
        ]
        rows = [[*(list(row))] for _, row in
                performance_df[
                    ['docker_type', 'MicroService', 'catalog', 'data', 'publish_date', 'version']].iterrows()]
        data = {
            "pfData": [ClearLinuxDefaultRunc, UbuntuDefaultRunc, CentOSDefaultRunc, ClearLinuxClearKata,
                       UbuntuClearKata, CentOSClearKata, ClearLinuxDefaultKata, UbuntuDefaultKata, CentOSDefaultKata,
                       ClearLinuxClearRunc, UbuntuClearRunc, CentOSClearRunc],
            "columns": columns,
            "rows": rows,
            "round": list(range(1, app.config['SIZE_ROUND'] + 1)),
            "micro": micro,
            "kpis": list(kpi_define.keys()),
            "units": units
        }
        return data


def store_performance(data):
    with db.auto_commit():
        performance = MicroPerformance()
        try:
            [setattr(performance, key, data[key]) for key in data.keys()]
            db.session.add(performance)
        except Exception as e:
            raise ServerError(e)


def get_httpd():
    pass


def get_python():
    pass
