#-*- coding: utf-8 -*-

from app import app


@app.route('/')
def rootDir():
    return 'ok'
