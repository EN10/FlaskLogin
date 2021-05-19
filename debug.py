from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/tables')
def tables():
	con = sqlite3.connect('login.db')
	cur = con.cursor()
	cur.execute("SELECT * FROM sqlite_master")
	rows = cur.fetchall()
	return str(rows)

@app.route('/insert', methods=['POST'])
def insert():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO Users (Username, Password) VALUES (?,?)",
                        (request.form['un'],request.form['pw']))
    except Exception as e:
        return str(e)
    con.commit()
    return request.form['un'] + ' added'


# print to pythonanywhere error log
# might be faster to run function() and click Run rather the Reload
import sys
print("fatal error", file=sys.stderr)
