from flask import request, Flask
import json

app = Flask(__name__)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)