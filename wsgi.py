from flask import Flask, request, redirect
from flask_login import (
    LoginManager
)
from flask_bootstrap import Bootstrap

import os

# Internal imports
from blueprints.google import google
from db import db
from models.user import User

login_manager = LoginManager()


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/users/google-oauth?next=' + request.path)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


def create_app():
    application = Flask(__name__)
    Bootstrap(application)
    application.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

    application.register_blueprint(google)

    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'

    db.init_app(application)
    login_manager.init_app(application)
    return application


def setup_app():
    app = create_app()
    with app.app_context():
        db.create_all()
    return app


if __name__ == "__main__":
    application = setup_app()
    application.run(ssl_context="adhoc")
