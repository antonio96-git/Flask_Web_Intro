from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()        # define the database (creating database object)
DB_NAME = 'database.db'  # naming the database

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fapofkopfkaopfa'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # setting location of the database
    db.init_app(app) # initialize database with our app

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    with app.app_context():
        db.create_all()


    return app

