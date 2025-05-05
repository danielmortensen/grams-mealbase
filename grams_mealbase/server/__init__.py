from flask import Flask
import os
from .ext import login_manager, bcrypt, migrate, db
from .auth import auth_blueprint

def create_app():
    app = Flask(__name__)

    # config parameters
    env = os.environ.get('FLASK_ENV', 'developement')
    if env == 'production':
        app.config.from_object('grams_mealbase.server.config.ProductionConfig')
    elif env == 'testing':
        app.config.from_object('grams_mealbase.server.config.TestingConfig')
    else:
        app.config.from_object('mealbase.server.config.DevelopementConfig')

    # general init
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app)
    db.init_app(app)

    # blueprints
    app.register_blueprint(auth_blueprint)
    return app

    