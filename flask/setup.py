#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 运行 FLASK_APP=flask/main.py flask run
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"