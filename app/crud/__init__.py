# -*- coding:utf-8 -*-
__author__ = '东方鹗'
__blog__ = u'http://www.os373.cn'


from flask import Blueprint


crud = Blueprint('crud', __name__, template_folder="templates", static_url_path='',
				 static_folder='templates/static')

# 在末尾导入相关模块，是为了避免循环导入依赖，因为在下面的模块中还要导入蓝本main
# from . import views
