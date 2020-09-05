from flask import Flask
from flask import render_template
import sqlite3
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/login')
def login():
	return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
	with sqlite3.connect('login.db') as db:
		cursor = db.cursor()
		cursor.execute(	"INSERT INTO Users (Username, Password) VALUES (?,?)",
			       		(request.form['uname'],request.form['psw']))
		db.commit()
	return request.form['uname'] + ' added'
	
@app.route('/create')
def create():
	with sqlite3.connect('login.db') as db:
		cursor = db.cursor()
		cursor.execute(	"""	CREATE TABLE Users(
						Username text,
						Password text,
						Primary Key(Username))
				""")
		db.commit()
	return 'CREATE'

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
	with sqlite3.connect('login.db') as db:
		cursor = db.cursor()
		cursor.execute(	"""	SELECT * FROM Users
				""")
		result = cursor.fetchall()
		if len(result) == 0:
			return 'no records'
		else:
			return ','.join(map(str, result))
