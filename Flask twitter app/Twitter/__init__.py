from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from Twitter.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app) 
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from Twitter.views.main.routes import main
    from Twitter.views.tweets.routes import tweets
    from Twitter.views.users.routes import user

    app.register_blueprint(main)
    app.register_blueprint(tweets)
    app.register_blueprint(user)

    return app