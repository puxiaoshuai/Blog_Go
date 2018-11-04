#注册蓝图
from flask import Flask
from  app.config import config
from  flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager
#sql等在这里进行初始化对象
db=SQLAlchemy()
login_manage=LoginManager()
login_manage.login_view='auth.login'

#导入home中的蓝图
def create_app(config_name):
    app_task = Flask(__name__)
    app_task.config.from_object(config[config_name])
    config[config_name].init_app(app_task)
    # 扩展应用初始化
    db.init_app(app_task)
    login_manage.init_app(app_task)
    #初始化蓝图
    from app.home import home as home_blueprint
    from app.auth import auth as auth_blueprint
    app_task.register_blueprint(home_blueprint)
    app_task.register_blueprint(auth_blueprint,url_prefix='/auth')
    # app_task.register_blueprint(xxx,url_prefix="/login")其他模块别名的表示/login进入登陆的路由板块

    return app_task




