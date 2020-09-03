from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method=='POST':
   		username = request.form['username']
   		password = request.form['password']
   		dbHandler.insertUser(username, password)
   		users = dbHandler.retrieveUsers()
		return render_template('index.html', users=users)
   	else:
   		return render_template('index.html')
