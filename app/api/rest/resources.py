"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request

from app.api.rest.base import BaseResource, SecureResource
from app.api import api


@api.route('/resource/<string:resource_id>')
class ResourceOne(BaseResource):
    """ Sample Resource Class """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

    def post(self, resource_id):
        json_payload = request.json
        return {'timestamp': json_payload}, 201


@api.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}
