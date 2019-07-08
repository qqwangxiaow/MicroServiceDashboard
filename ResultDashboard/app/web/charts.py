from flask import render_template, request, url_for, redirect
from flask_login import current_user, logout_user, login_required

from .blueprint import web


@web.route('/index')
@web.route('/')
def index():
    return render_template("index.html")


@web.route('/performance')
# @login_required
def performance():
    return render_template("performance.html")


@web.route('/realtime')
# @login_required
def realtime():
    return render_template("realtime.html")


@web.route('/details')
# @login_required
def details():
    return render_template("details.html")


@web.route('/size')
# @login_required
def size():
    return render_template("size.html")


