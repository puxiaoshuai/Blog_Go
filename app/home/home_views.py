from app.home import home
from app.config import *
from app import create_app
app_task=create_app("default")
app_task.config.from_object(Config)
@home.route("/")
def home():
    return app_task.config.get("TEST_KEY")