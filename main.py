from flask import Flask, render_template, request, session
from datetime import timedelta
import sqlite3
import os
from markupsafe import escape

app = Flask(__name__)
app.secret_key = os.urandom(16)
session.permanent = True
app.permanent_session_lifetime = timedelta(minutes=1)
		
@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/login')
def login():
	return render_template('index.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

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
create()

@app.route('/insert')
def insert():
	with sqlite3.connect('login.db') as db:
		cursor = db.cursor()
		cursor.execute(	"""	INSERT INTO Users (Username, Password)
						VALUES ("Bob", "123")
				""")
		db.commit()
	return 'INSERT'

@app.route('/select')
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

@app.route('/add', methods=['POST'])
def add():
	with sqlite3.connect('login.db') as db:
		cursor = db.cursor()
		cursor.execute(	"INSERT INTO Users (Username, Password) VALUES (?,?)",
			       		(request.form['uname'],request.form['psw']))
		db.commit()
	return request.form['uname'] + ' added'

@app.route('/verify', methods=['POST'])
def verify():
	with sqlite3.connect('login.db') as db:
		cursor = db.cursor()
		cursor.execute(	"SELECT * FROM Users WHERE Username=? AND Password=?",
			       (request.form['uname'],request.form['psw']))
		result = cursor.fetchall()
		if len(result) == 0:
			return 'username / password not recognised'
		else:
			session['username'] = request.form['uname']
			return 'welcome ' + request.form['uname']
@app.route('/cookie')
def cookie():
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])
	return 'You are not logged in'

