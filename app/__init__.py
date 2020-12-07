from flask_restx import Api
from flask import Blueprint

from .main.controller.id_controller import api as client_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='TP_CleanCode API',
          version='1.0',
          description='Evaluated API'
          )

api.add_namespace(client_ns, path='/client')
