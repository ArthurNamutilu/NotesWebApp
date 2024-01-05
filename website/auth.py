from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<h1>auth..</h1>"


@auth.route('/logout')
def logout():
    return "<h1>Logging out</h1>"


@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"
