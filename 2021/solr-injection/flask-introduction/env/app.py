from flask import Flask, render_template, redirect, url_for, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin-console')
def admin():
    if request.authorization and request.authorization.username == 'ctf' and request.authorization.password == 'P@ssw0rd!':
        return redirect('http://localhost:8983/solr/#/', code=302)
    else:
        return make_response('Could not verify!' , 401, {'WWW-Authenticate':'Basic realm="Login Required"'})

if __name__ == "__main__":
    app.run()