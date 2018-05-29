import os
from flask import Flask
import click

from app import client, api, commands
from app.extensions import db, migrate
from app.config import ProdConfig


def create_app(config_object=ProdConfig):

    app = Flask(__name__)
    app.config.from_object(config_object)
    app.logger.info('>>> {0}'.format(config_object))

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_shellcontext(app)
    register_errorhandlers(app)

    return app


def register_extensions(app):

    db.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):

    app.register_blueprint(api.blueprint)
    app.register_blueprint(client.blueprint)
    return None


def register_commands(app):

    app.cli.add_command(commands.test)
    app.cli.add_command(commands.serve_client)
    app.cli.add_command(commands.build_client)
    return None


def register_errorhandlers(app):
    pass


def register_shellcontext(app):
    def shell_context():
        return {
            'Hello': 'World!',
            'db': db
        }
    app.shell_context_processor(shell_context)
