#! /usr/bin/env python3.6
# author: XiaHuaLou
# Create Time: 4/24/19 11:00 PM

from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=app.config['DEBUG'])
