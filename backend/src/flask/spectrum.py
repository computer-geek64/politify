#!/usr/bin/python3 -B
# spectrum.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import psycopg2
from flask import Blueprint, request, jsonify
from config import DB_NAME, DB_USER, DB_PASSWORD


spectrum_blueprint = Blueprint('spectrum_blueprint', __name__, template_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates'), static_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static'))


# Display people on political spectrum
@spectrum_blueprint.route('/people/', methods=['GET'])
def get_spectrum():
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    conn.close()
