import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #we use environment variable and in case not defined or statement is used
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS  = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER' or 'localhost')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('sahilkundu.1234@gmail.com')
    MAIL_PASSWORD = os.environ.get('sahil@sahilkundu')
    ADMINS = ['sahilkundu.1234@gmail.com']
    #LANGUAGES = ['en', 'es']

    POSTS_PER_PAGE = 3