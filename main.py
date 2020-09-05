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

@app.route('/view', methods=['POST'])
def view():
	print(request.form['psw'])
	return request.form['psw']
	
@app.route('/create')
def create():
	with sqlite3.connect('coffee_shop.db') as db:
		cursor = db.cursor()
		cursor.execute(	"""	CREATE TABLE Product(
						ProductID integer,
						Name text,
						Price real,
						Primary Key(ProductID))
				""")
		db.commit()
	return 'CREATE'

@app.route('/insert')
def insert():
	with sqlite3.connect('coffee_shop.db') as db:
		cursor = db.cursor()
		cursor.execute(	"""	INSERT INTO Product (Name, Price)
						VALUES ("Apple Juice", 10.4)
				""")
		db.commit()
	return 'INSERT'

@app.route('/select')
def select():
	with sqlite3.connect('coffee_shop.db') as db:
		cursor = db.cursor()
		cursor.execute(	"""	SELECT * FROM Product
				""")
		result = cursor.fetchall()
		#printable = ','.join(map(str, result))	# from list to string
	return ','.join(map(str, result))
