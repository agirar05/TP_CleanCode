from flask import request, Flask
from flask_restplus import Api, Resource, fields
import json

app = Flask(__name__)
api = Api(app, version="1.0", title='CleanCode API', description='Evaluated API')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)