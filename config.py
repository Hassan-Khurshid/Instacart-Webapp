class Config(object):
    DEBUG = False
    TESTING = False

    db_username = 'group3'
    db_password = 'group3pw!'
    db_host = 'instacart-db.cbujeonilgtq.us-east-2.rds.amazonaws.com'
    db_db = 'cs527_instacart'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(db_username, db_password, db_host, db_db)

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass