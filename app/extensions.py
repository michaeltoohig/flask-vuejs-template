# -*- coding: utf-8 -*-

import flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

db = SQLAlchemy()
migrate = Migrate()

