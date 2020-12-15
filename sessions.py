from flask import Flask, request, session
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(seconds=10)

@app.route('/')
def login():
    password = request.args.get('p', '')
    if password == '123':
        session.permanent = True
        session['loggedin'] = 'True'
        return 'welcome'
    return 'error'

@app.route('/logged')
def logged():
    if 'loggedin' in session:
        return 'you are logged in'
    return 'You are not logged in'

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    return "you've been logged out"
