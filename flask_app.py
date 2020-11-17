from flask import Flask
from flask import render_template
import sqlite3
from flask import request

app = Flask(__name__)

@app.route('/create')
def create():
	con = sqlite3.connect('login.db')
	cur = con.cursor()
	cur.execute(	"""	CREATE TABLE Users(
					Username text,
					Password text,
					Primary Key(Username))
			""")
	con.commit()
	return 'CREATE'

@app.route('/insert')
def insert():
	con = sqlite3.connect('login.db')
	cur = con.cursor()
	cur.execute(	"""	INSERT INTO Users (Username, Password)
					VALUES ("Bob", "123")
			""")
	con.commit()
	return 'INSERT'

@app.route('/select')
def select():
	con = sqlite3.connect('login.db')
	cur = db.cursor()
	cur.execute("SELECT * FROM Users")
	rows = cur.fetchall()
	return str(rows)
