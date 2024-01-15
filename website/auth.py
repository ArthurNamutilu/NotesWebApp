from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/logout')
def logout():
    return render_template("logout.html")


@auth.route('/log-in', methods=['GET', 'POST'])
def login():
    data = request.form

    return render_template("log_in.html")


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 chracters', category='error')
        elif len(firstname) < 4:
            flash('First name must be greater than 3 characters', category='error')
        elif password1 != password2:
            flash('Your password do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be atleast 7 characters', category='error')
        else:
            flash('Account succesfully created', category='success')

    return render_template("sign_up.html")
