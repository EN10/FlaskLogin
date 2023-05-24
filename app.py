from flask import Flask, render_template, request, session
import sqlite3
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)

@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
    else:
        username = "not logged in"
    return render_template('index.html', username=username)

@app.route('/logout')
def logout():
    session.pop("username")
    return "logged out!"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/select', methods=['POST'])
def select():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("""
    SELECT * FROM login
    WHERE username = ? AND password = ?
    """, (request.form['username'], request.form['password']))
    rows = cur.fetchall()
    if len(rows) == 1:
        session['username'] = request.form['username']
        return "welcome " + request.form['username']
    else:
        return "Login not recognised!"

@app.route('/insert', methods=['POST'])
def insert():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("""
    INSERT INTO login (username, password)
    VALUES (?, ?)
    """, (request.form['username'], request.form['password']))
    con.commit()
    return 'signup successful'

@app.route('/bob')
def bob():
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
