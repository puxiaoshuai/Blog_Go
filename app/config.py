import os
basedir=os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY=os.environ.get("SECRET_KEY") or "puxiaoshuai123"
    # 当关闭数据库是否自动提交事务
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 是否追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #
    SQLALCHEMY_ECHO=True
    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql://root:puhao@localhost/blog?charset=utf8'
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:puhao@localhost/blog?charset=utf8'
config={
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}