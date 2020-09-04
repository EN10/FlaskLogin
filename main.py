import sqlite3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!1'

@app.route('/create')
def create_table():
    sql = """   CREATE TABLE Product(
				ProductID integer,
				Name text,
				Price real,
				Primary Key(ProductID))
          """
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
    return 'CREATE TABLE'
