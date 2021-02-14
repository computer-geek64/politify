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

    cursor.execute('''
SELECT *
  FROM person;
''')
    people = sorted([{
        'handle': person[0],
        'name': person[1],
        'description': person[2],
        'picture': person[3],
        'score': person[4]
    } for person in cursor.fetchall()], key=lambda x: x['score'])

    current_sum = 0
    for i in range(len(people)):
        people[i]['score'] -= current_sum
        current_sum += people[i]['score']

    conn.close()

    json_response = {
        'min': 0,
        'max': 1,
        'people': people
    }

    return jsonify(json_response), 200
