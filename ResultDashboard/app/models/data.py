# -*- coding: utf-8 -*-
# Author  : XiaHuaLou
# Email   : hualoux.xia@intel.com
# Create timeTime    : 6/3/19 11:36 PM
from .base import BaseData
from sqlalchemy import Column, Integer, String, Enum, DateTime, SmallInteger, Float
from datetime import datetime
from app.libs.enums import MicroServiceEnum


class MicroSizeData(BaseData):
    id = Column(Integer, primary_key=True, autoincrement=True)
    docker_type = Column(String(64), nullable=False)
    micro_code = Column(SmallInteger, nullable=False)
    size = Column(Float(), nullable=False)
    version = Column(String(64), nullable=False)
    catalog = Column(String(64))
    OS = Column(Enum("ClearLinux", 'Ubuntu', 'CentOS'))
    publish_date = Column(DateTime, default=datetime.now())


class MicroPerformance(BaseData):
    id = Column(Integer, primary_key=True, autoincrement=True)
    docker_type = Column(String(64), nullable=False)
    micro_code = Column(SmallInteger, nullable=False)
    version = Column(String(64), nullable=False)
    catalog = Column(String(64))
    OS = Column(Enum("ClearLinux", 'Ubuntu', 'CentOS'))
    publish_date = Column(DateTime, nullable=False)
    data = Column(Float(), nullable=False)
    kpi = Column(String(64), nullable=False)


class HostConfig(BaseData):
    id = Column(Integer, primary_key=True, autoincrement=True)
    OS = Column(Enum("ClearLinux", 'Ubuntu', 'CentOS'))
    Processor = Column(SmallInteger)
    Core = Column(SmallInteger)
    Threads = Column(SmallInteger)
    InstructionsSet = Column(SmallInteger)
    Memory = Column(String(64))
    Storage = Column(String(64))
    NetWork = Column(String(128))
