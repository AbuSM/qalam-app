import flask
import sqlite3
import os
import os.path
from flask import request, jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "requests.db")

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

API = '/api/v1/{}'

@app.route(API.format('request'), methods=['POST'])
def main():
	print("Got request: ", request.form)
	name = request.form.get('name')
	email = request.form.get('email')
	phone = request.form.get('phone')
	message = request.form.get('message')

	conn = sqlite3.connect(db_path)
	conn.row_factory = dict_factory
	cur = conn.cursor()
	print(12312)
	cur.execute(f"INSERT INTO requests(name, phone, email, message) values('{name}', '{phone}', '{email}', '{message}')")
	conn.commit()
	return 'Success'

app.run()