from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
