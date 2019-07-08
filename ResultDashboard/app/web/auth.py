# _*_coding:utf-8_*
# author: XiaHuaLou
# Create Time: 4/24/19 11:00 PM

from flask import render_template, request, url_for, redirect, flash
from flask.json import jsonify
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User, db

from .blueprint import web


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


@web.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.login'))


@web.route('/test')
def test():
    return render_template("test.html")
