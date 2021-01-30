import flask
import sqlite3
import os
import os.path
from flask import request, jsonify, render_template
from flask_cors import CORS, cross_origin

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "requests.db")

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app, resources={r"/api/*": {"origins": "*"}})

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

API = '/api/v1/{}'

@app.route(API.format('requests'), methods=['POST', 'OPTIONS'])
def main():
	print("Got request: ", request.form)
	name = request.form.get('name')
	email = request.form.get('email')
	phone = request.form.get('phone')
	message = request.form.get('message')

	conn = sqlite3.connect(db_path)
	conn.row_factory = dict_factory
	cur = conn.cursor()

	cur.execute(f"INSERT INTO requests(name, phone, email, message) values('{name}', '{phone}', '{email}', '{message}')")
	conn.commit()
	return jsonify(dict({"message": "ok"}))

if __name__ == '__main__':
	app.run()