
import os

from app import create_app
from flask_script import Manager ,Shell

app_task=create_app(os.getenv('FLASK_CONFIG') or 'default')
#集成python shell ,就不用每次导入模型了，数据库实例等
'''manager=Manager(app_task)
def make_shell_context():
    return dict(app=app_task,db=db)
manager.add_command("shell", Shell(make_context=make_shell_context))
#manager.add_command('db', MigrateCommand)
'''

if __name__ == '__main__':

    app_task.run(port=1100)
