from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/db')
def create():
	con = sqlite3.connect('example.db')
	con.commit()
	return 'DB Created'
