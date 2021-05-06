from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        name = request.form['un']
        return 'hello ' + name
    else:
        return render_template('simple_form.html')
