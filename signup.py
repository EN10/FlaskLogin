from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        con = sqlite3.connect('login.db')
        cur = con.cursor()
		cur.execute("INSERT INTO Users (Username, Password) VALUES (?,?)",
			       		(request.form['un'],request.form['pw']))
        con.commit()
        return request.form['un'] + ' added'
    else:
        return render_template('simple_form.html')
