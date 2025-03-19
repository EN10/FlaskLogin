from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'random'

@app.route('/')
def home():
    if 'username' in session:
        return render_template('welcome.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'GET': 
        return render_template('simple_form.html')
    con = sqlite3.connect('login.db') 
    cur = con.cursor() 
    cur.execute("SELECT * FROM Users WHERE Username=? AND Password=?", 
                (request.form['un'], request.form['pw'])) 
    results = cur.fetchall()

    if not results: 
        return "Wrong username and password" 
    else: 
        session['username'] = request.form['un'] 
        return render_template('welcome.html')

@app.route('/logout') 
def logout(): 
    session.pop('username', None) 
    return redirect(url_for('login')) 

if __name__ == "__main__":
    app.run(debug=True)