#!/usr/bin/python3

from flask import Flask, jsonify, make_response, request
from random import randrange

app = Flask(__name__)

vals = {'shaperValue': randrange(80,100), 'bandwidth': randrange(80,100)}

@app.route("/api/vals/", methods=['GET'])
def get_shaperValue():
    return jsonify({'vals': vals})

@app.route("/api/shaperValue/", methods=['PUT'])
def update_shaperValue():
    if 'shaperValue' in request.json and type(request.json['shaperValue']) is not int:
            abort(400)
    vals['shaperValue'] = request.json.get('shaperValue')
    return jsonify({'vals': vals}), 201

@app.route("/")
def index():
    return "Hello, world!"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(debug=True)
