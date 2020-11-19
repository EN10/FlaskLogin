from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/tables')
def tables():
	con = sqlite3.connect('login.db')
	cur = con.cursor()
	cur.execute("SELECT * FROM sqlite_master")
	rows = cur.fetchall()
	return str(rows)
