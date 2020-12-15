from flask import Flask, request, session
from os import urandom
from datetime import timedelta

app = Flask(__name__)
app.secret_key = urandom(16)
app.permanent_session_lifetime =  timedelta(seconds=10)

@app.route('/')
def login():
    if request.args.get('p', '') == '123':
        session['loggedin'] = True
        return 'Welcome'
    elif 'loggedin' in session:
        return 'You are logged in'
    return 'You are not logged in'

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    return "You've been logged out"
