#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route('/')
def output():
    return render_template("index.html", name="Taras")

@app.route('/reciever', methods = [ 'POST' ])
def worker():
    data = request.get_jason()
    result = ''

    for item in data:
        result += str(item['make']) + '\n'

if __name__ == "__main__":
    app.run('0.0.0.0', '5010')
