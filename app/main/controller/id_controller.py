"""id_controller.py: The endpoint of the api, call function when request are made"""
__author__      = "Girard Alexandre"

from flask import request
from flask_restx import Resource

from ..util.idDto import IDDto
api = IDDto.api

from ..service.verify_id_service import checkID
from ..service.create_id_service import createID

@api.route('/cle/verification')
@api.doc(params={'id': 'An ID to verify'}, location='query')
class VerifyID(Resource):
    @api.doc('Verify an id')
    def get(self):
        """Verify an id"""
        return checkID(request.args.get('id'))


@api.route('/cle/creation')
@api.doc(params={'id': 'Numbers of an ID to generate'}, location='query')
class CreateID(Resource):
    @api.doc('Create an id')
    def get(self):
        """Create an id"""
        return createID(request.args.get('id'))