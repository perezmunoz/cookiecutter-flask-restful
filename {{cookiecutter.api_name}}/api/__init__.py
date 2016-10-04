# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask_appconfig import AppConfig
from flask_sqlalchemy import SQLAlchemy

import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask('{{cookiecutter.app_name}}')
api = Api(app)
AppConfig(app, os.path.join(basedir, 'default_config.py'))
db = SQLAlchemy(app)

from api import models
from api.views import randomirisapi
