# -*- coding:utf-8 -*-

import os
import sys
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

__author__ = '东方鹗'
__blog__ = u'http://www.os373.cn'

from flask import Flask
import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    """ 使用工厂函数初始化程序实例"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app=app)

    db.init_app(app=app)

    # 注册蓝本crud
    # from .crud import crud as crud_blueprint
    # app.register_blueprint(crud_blueprint, url_prefix='/crud')
    from app.crud.views import crud
    app.register_blueprint(crud)

    return app
