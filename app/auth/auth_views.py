from flask import render_template, request, flash, redirect, url_for

from app.auth.forms import Login
from app.home.models import User
from . import auth
from flask_login import login_required, login_user


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = Login(request.form)
    if request.method == "POST":
        if form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None and user.verify_pwd(form.email.data):
                login_user(user, form.rember_me.data)
                return redirect(url_for('home.home'))
            else:
                flash("该账号不存在，请重试")
                return render_template('login/login.html')
    else:
        pass
    return render_template('login/login.html')


@auth.route('/secret')
@login_required
def secret():
    return "only login"
