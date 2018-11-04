from wtforms import StringField, PasswordField, BooleanField, SubmitField, Form
from wtforms.validators import DataRequired, length, Email


class Login(Form):
    email = StringField('Email', validators=[DataRequired(), length(10, 16), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    rember_me = BooleanField("记住密码")
