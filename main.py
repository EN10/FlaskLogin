from flask import Flask, render_template, session, redirect, url_for
import os
from markupsafe import escape
from datetime import timedelta
import sql

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=1)
		
@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/login')
def login():
	return render_template('index.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

sql.create()

@app.route('/insert')
def insert():
	return sql.insert()

@app.route('/select')
def select():
	return sql.select()

@app.route('/add', methods=['POST'])
def add():
	return sql.add()

@app.route('/verify', methods=['POST'])
def verify():
	return sql.verify()

@app.route('/un')
def un():
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])
	return 'You are not logged in'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('un'))
