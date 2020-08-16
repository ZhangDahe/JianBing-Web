import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' #从环境变量中获取配置变量.拿不到就使用默认值
    print(basedir)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS = ['your-email@example.com']

    MAIL_SERVER = 'smtp.126.com'

    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USERNAME = "zyanhe@126.com"
    MAIL_PASSWORD = "ZSIWXRRYTBTWVOZD"
    ADMINS = ['zyanhe@126.com']   #发件地址
    RECV_MAIL = ['347834800@qq.com']  # 收件地址

    LANGUAGES = ['en', 'zh']

    POSTS_PER_PAGE = 3