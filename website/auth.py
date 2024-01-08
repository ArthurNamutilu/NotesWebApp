from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/logout')
def logout():
    return render_template("logout.html")


@auth.route('/log-in')
def login():
    return render_template("log_in.html")


@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
