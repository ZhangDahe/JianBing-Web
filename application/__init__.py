#__init__.py 文件的作用是将文件夹变为一个Python模块
''''自己有改动'''
from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy#ORM 第四章
from flask_migrate import Migrate  #数据库迁移引擎 第四章

from flask_login import LoginManager #用户登录 第五章

import logging
from logging.handlers import SMTPHandler,RotatingFileHandler # 第七章 日志模块
import os
from flask_mail import Mail
from flask_bootstrap import Bootstrap

from flask import request
from flask_babel import Babel
from flask_moment import Moment



app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)# 返回啥
migrate = Migrate(app, db)#同上
login = LoginManager(app)
login.login_view = 'login'

mail = Mail(app)  #传入app,以实现对mail的初始化
bootstrap = Bootstrap(app)


babel = Babel(app)
moment = Moment(app)
if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
         #   fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            fromaddr= app.config['MAIL_USERNAME'],
            toaddrs=app.config['RECV_MAIL'],
            subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

from application import routes, models,errors  # model功能