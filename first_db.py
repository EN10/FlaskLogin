from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/create')
def create():
	con = sqlite3.connect('login.db')
	cur = con.cursor()
	cur.execute(	"""	CREATE TABLE Users(
					Username VARCHAR(20) NOT NULL PRIMARY KEY,
					Password VARCHAR(20) NOT NULL
						  )
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
	cur = con.cursor()
	cur.execute("SELECT * FROM Users")
	rows = cur.fetchall()
	return str(rows)
