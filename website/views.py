from flask import Blueprint, render_template

views = Blueprint('views', __name__)

""" decorator associates following function with specific url route within the blueprint"""


@views.route('/')
def home():
    return render_template("home.html")
