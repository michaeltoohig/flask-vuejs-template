""" API Blueprint Application """

import os
from flask import Flask, Blueprint, session, current_app
from flask_restplus import Api

blueprint = Blueprint('api', __name__,
                   template_folder='templates',
                   url_prefix='/api')

api = Api(blueprint)

@blueprint.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'

    # Required for Webpack dev application to make  requests to flask api
    # from another host (localhost:8080)
    if not current_app.config['PRODUCTION']:
        response.headers['Access-Control-Allow-Origin'] = '*'
    return response

from app.api.rest import resources
