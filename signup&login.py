from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3

@app.route('/')
def home():
        return render_template('simple_form.html')

@app.route('/signup', methods=['POST'])
def signup():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("INSERT INTO Users (Username, Password) VALUES (?,?)",
                    (request.form['un'],request.form['pw']))
    con.commit()
    return request.form['un'] + ' added'

@app.route('/login', methods=['POST'])
def login():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Users WHERE Username=? AND Password=?",
                    (request.form['un'],request.form['pw']))
    match = len(cur.fetchall())
    if match == 0:
        return "Wrong username and password"
    else:
        return "Welcome " + request.form['un']
