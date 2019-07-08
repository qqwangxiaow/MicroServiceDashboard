# _*_coding:utf-8_*
# author: XiaHuaLou
# Create Time: 4/24/19 11:00 PM
from http.client import HTTPException
from flask_login import LoginManager

from app.app import Flask
from app.libs.error import APIException
from app.libs.error_code import ServerError

login_manager = LoginManager()
from app.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.settings')
    # register blueprint
    register_blueprint(app)
    # register plugin
    register_plugin(app)
    # register db
    db.init_app(app)
    # register login module
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    # login_manager.login_message = 'Please Login Firstly'
    return app


def register_plugin(app):
    from app.models.base import db
    from app.cache import cache
    db.init_app(app)
    cache.init_app(app,app.config['CACHE_CONFIG'])
    with app.app_context():
        db.create_all()
    pass


def register_blueprint(app):
    from app.web.blueprint import web
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(web)
    # register redPrint to BluePrint
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        if app.config['DEBUG']:
            raise e
        return ServerError()
