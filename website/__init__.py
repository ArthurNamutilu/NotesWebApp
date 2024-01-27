from flask import Flask
from os import path
from .views import views
from .auth import auth
from flask_sqlalchemy import SQLAlchemy
from .db import db
from flask_login import LoginManager

# db = SQLAlchemy()
DB_NAME = "store.db"


def create_app():  # application factory - func creates a Flask app instance
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'djncdoncen'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # registering blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader()
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Okay Database created')
