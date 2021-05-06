from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name', '')
    if name == '':
        return render_template('simple_form.html')
    else:
        return 'hello ' + name
