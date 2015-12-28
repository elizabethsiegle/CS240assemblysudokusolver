#!/usr/bin/env python
# http://flask.pocoo.org/docs/0.10/quickstart/
# http://jinja.pocoo.org/docs/dev/templates/
import os
from flask import Flask, session, render_template, url_for, redirect, request, flash


app = Flask(__name__)
app.secret_key = os.urandom(24)

return_string = 'Hello World!!!'

@app.route('/', methods=['GET'])
def index():
    return render_template('twitter.html')

@app.route('/', methods=['GET'])
def hello_world():
    if request.form:
        username = request.form['username']
        return render_template('twitter.html', username=username)
    else:
        return "ERROR"



if __name__ == '__main__':
    app.run(debug=True)
