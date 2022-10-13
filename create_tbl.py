import sqlite3
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    con = sqlite3.connect("login.db")
    cur = con.cursor()
    try:
        cur.execute("""
        CREATE TABLE Users(
        Username VARCHAR(20) NOT NULL PRIMARY KEY,
	Password VARCHAR(20) NOT NULL)
        """)
    except sqlite3.OperationalError as e:
        return str(e)
    return "table created"
