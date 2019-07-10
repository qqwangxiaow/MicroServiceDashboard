# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 5/29/19 9:34 PM
from app.libs.error_code import MicroServiceNotFoundError, ServerError
from app.models.data import MicroSizeData
from app.libs.enums import MicroServiceEnum
from flask import current_app as app
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
            "kpis": getattr(KPI,micro),
            "micro": micro,
        }
    return data


def get_performance(micro_code):
    j = {
        'performanceData': [[200, 200, 100, 400, 500, 600, 700], [300, 200, 400, 200, 300, 200, 100],
                            [500, 510, 300, 200, 300, 400, 500]]
    }
    return j


def get_httpd():
    j = {
        'columns': [
            {"title": 'MicroService'},
            {"title": "Catalog"},
            {"title": "Performance"},
        ],
        "rows": [
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
        ]
    }
    return j


def get_python():
    j = {'columns': [
        {"title": 'MicroService'},
        {"title": "Catalog"},
        {"title": "Performance"},
    ],
        "rows": [
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
            ['HTTPD', 'web', '43MB', ],
        ]
    }
    return j
