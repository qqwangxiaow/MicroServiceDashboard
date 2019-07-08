# _*_coding:utf-8_*
# author: XiaHuaLou
# Create Time: 4/24/19 11:05 PM
from .base import Base
from sqlalchemy import Column, Integer, String


class Test01(Base):
    __tablename__ = 'test01'

    id = Column(Integer, primary_key=True, autoincrement=True)
    MicroService = Column(String(50), nullable=False)
    Category = Column(String(64))
    Clear_Bundle = Column(String(64))
    Clear_Packge = Column(String(64))
    Performance = Column(String(64))
    Size = Column(String(64))
    Comment = Column(String(256))
