from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("""
    INSERT INTO login (username, password)
    VALUES (?, ?)
    """,
    (request.form['username'], request.form['password'])
    )
    con.commit()
    return 'signup successful'

@app.route('/insert')
def insert():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("""
    INSERT INTO login (username, password)
    VALUES ("bob", "123")
    """)
    con.commit()
    return 'bob added'

@app.route('/table')
def table():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE login
    (
    username VARCHAR(20) NOT NULL PRIMARY KEY,
    password VARCHAR(20) NOT NULL
    )
    """)
    return 'table created!'
