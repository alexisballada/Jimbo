from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/updates')
def suggestions():
    text = "whatever variable"
    
    return render_template('index.html', text)


@app.route('/return', methods=['POST'])
def samplefunction():
    output = request.form['output']
    print ( output )
    return output
        
    text = output


if __name__ == '__main__':
   app.run(debug = True)
