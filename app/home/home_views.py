from app.home import home
from app.config import *
from app import create_app
from flask import  render_template

app_task = create_app("default")
app_task.config.from_object(Config)


@home.route("/")
def home():
    return  render_template('home/home.html')
