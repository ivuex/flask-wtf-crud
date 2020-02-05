# -*- coding:utf-8 -*-
__author__ = '东方鹗'
__blog__ = u'http://www.os373.cn'

import os
from app import create_app, db
from app.models import User
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

# # app = Flask(__name__, static_folder='static', static_url_path='/static')
# from flask import Flask
# app = Flask(__name__)
# app.config["SECRET_KEY"] = "hskghsaklg"


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app=app)
migrate = Migrate(app=app, db=db)

from app.crud.views import crud
app.register_blueprint(crud)



def make_shell_context():
    return dict(app=app, db=db, User=User)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """ 单元测试 """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(test=tests)


if __name__ == '__main__':
    manager.run()
