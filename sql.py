from flask import request, session
import sqlite3

def create():
	with sqlite3.connect('login.db') as db:
		cursor = db.cursor()
		cursor.execute(	"""	CREATE TABLE IF NOT EXISTS Users(
						Username text,
						Password text,
						Primary Key(Username))
				""")
		db.commit()
	print('CREATE')

def insert():
	with sqlite3.connect('login.db') as db:
		cursor = db.cursor()
		cursor.execute(	"""	INSERT INTO Users (Username, Password)
						VALUES ("Bob", "123")
				""")
		db.commit()
	return 'INSERT'

def select():
	try:
		with sqlite3.connect('login.db') as db:
			cursor = db.cursor()
			cursor.execute("SELECT * FROM Users")
			result = cursor.fetchall()
			if len(result) == 0:
				return 'no records'
			else:
				return ','.join(map(str, result))
	except Exception as e:
		return str(e)

def add():
	with sqlite3.connect('login.db') as db:
		cursor = db.cursor()
		cursor.execute(	"INSERT INTO Users (Username, Password) VALUES (?,?)",
			       		(request.form['uname'],request.form['psw']))
		db.commit()
	return request.form['uname'] + ' added'

def verify():
	with sqlite3.connect('login.db') as db:
		cursor = db.cursor()
		cursor.execute(	"SELECT * FROM Users WHERE Username=? AND Password=?",
			       (request.form['uname'],request.form['psw']))
		result = cursor.fetchall()
		if len(result) == 0:
			return 'username / password not recognised'
		else:
			session.permanent = True
			session['username'] = request.form['uname']
			return 'welcome ' + request.form['uname']
