from flask import Blueprint
home=Blueprint('home',__name__)
import app.home.home_views #导入路由文件
import app.home.errors#导入错误信息