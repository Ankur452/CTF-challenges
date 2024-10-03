from flask import Flask,render_template,redirect, url_for, send_file, make_response,request
import json
import os
import urllib.parse

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return redirect("/home", code = 302)

@app.route('/home')
def welcome():
    return render_template('index.html')

@app.route("/terms_and_conditions", methods = ['GET'])
def terms_and_conditions():
    tac = request.args.get('tac')
    return send_file('static/terms_and_conditions/'+tac, attachment_filename=tac)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/login_submittion", methods = ['GET','POST'])
def login_submittion():
    if request.method == "POST":
        username = urllib.parse.unquote(request.form.get("username"))
        password = urllib.parse.unquote(request.form.get("password"))

        if username == 'sysadmin@power.com' and password == 'CTFdumpP@ssw0rd123!':
            return redirect('/financial_data/', code = 302)
        else:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)
    else:
        error = 'Invalid Method used.'
        return render_template('login.html', error=error)

@app.route('/financial_data/')
def financial_data():
    return render_template("financial_data.html")

@app.route('/show_record')
def show_records():
    record = request.args.get('record')
    return send_file('static/financial_data/'+record, attachment_filename=record)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', code=404)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")