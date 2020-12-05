from flask_restx import Api
from flask import Blueprint

from .main.controller.id_controller import api as id_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='UFO API',
          version='1.0',
          description='a well designed Flask API ...'
          )

api.add_namespace(id_ns, path='/cle')
