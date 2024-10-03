from pickle import TRUE
from flask import Flask,render_template,redirect, url_for, send_file, make_response,request
from datetime import date
import subprocess
import json
import os

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return redirect("/dashboard", code = 302)

@app.route('/home', methods = ['POST', 'GET'])
def home():
    method_name = request.args['help']
    # output = os.system(method_name)
    output = subprocess.check_output(method_name, shell = TRUE).rstrip()
    print(output)
    return render_template('index.html', output=output)

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', code=404)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")