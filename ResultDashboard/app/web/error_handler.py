# _*_coding:utf-8_*
# author: XiaHuaLou
# Create Time: 5/12/19 11:00 PM


from flask import render_template

from .blueprint import web


@web.app_errorhandler(404)
def handle_404_error(error):
    return render_template('404.html'), 404


@web.app_errorhandler(500)
def handle_500_error(error):
    return render_template('500.html'), 500


@web.app_errorhandler(403)
def handle_403_error(error):
    return render_template('403.html'), 403
