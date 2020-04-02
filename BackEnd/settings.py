import os

basedir = os.path.abspath(os.path.dirname(__file__))


def get_dbinfo(dbinfo):
    engine = dbinfo.get('ENGINE')
    driver = dbinfo.get('DRIVER')
    db_name = dbinfo.get('DB_NAME')
    user = dbinfo.get('USER')
    password = dbinfo.get('PASSWORD')
    host = dbinfo.get('HOST')
    port = dbinfo.get('PORT')
    return '{}+{}://{}:{}@{}:{}/{}'.format(engine, driver, user, password, host, port, db_name, )


class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    DEBUG = True
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'DB_NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
    SQLALCHEMY_DATABASE_URI = get_dbinfo(dbinfo)


class Testing(Config):
    TESTING = True
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'DB_NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
    SQLALCHEMY_DATABASE_URI = get_dbinfo(dbinfo)


class Production(Config):
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'DB_NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
    SQLALCHEMY_DATABASE_URI = get_dbinfo(dbinfo)


envs = {
    'development': Development,
    'testing': Testing,
    'production': Production,
    'default': Development
}
