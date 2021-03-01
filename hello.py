from flask import Flask
from flask import request
app = Flask(__name__)



@app.route('/')
def goodbye_world():
    return 'Goodbye, World!'


@app.route('/hello')
def hello_world():
    return 'Hello, World!!!!!'

@app.route


# @app.route('/getRequest')