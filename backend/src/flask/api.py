#!/usr/bin/python3 -B
# api.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import IP, PORT
from flask_cors import CORS
from flask import Flask, request, jsonify


app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates'), static_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static'))
CORS(app)


# Home
@app.route('/', methods=['GET'])
def get_home():
    return 'Welcome to Politify!', 200


if __name__ == '__main__':
    app.run(IP, PORT)
