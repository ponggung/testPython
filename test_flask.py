from flask import Flask, get_flashed_messages, flash
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask import jsonify
import time
import json
app = Flask(__name__)
CORS(app)

data = {"a":123}

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/foo")
def foo():
    return jsonify(data)

@app.route("/get/<key>")
def get(key):
    value = data.get(key)
    return value


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)