from flask import Flask,render_template,redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return redirect("/welcome-to-our-casino", code = 302)

@app.route('/welcome-to-our-casino')
def welcome():
    return render_template('index.html')

@app.route('/', subdomain='hint')
def hint():
    return "Nothing to find here"

# @app.route('/', subdomain='ctf')
# def ctf():
#     return "Got your flag?"

if __name__ == "__main__":
    app.run(host='casino.ctf')