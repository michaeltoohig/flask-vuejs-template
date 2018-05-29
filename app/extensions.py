# -*- coding: utf-8 -*-

import flask

from flask_security import Security
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand


security = Security()
db = SQLAlchemy()
migrate = Migrate()

