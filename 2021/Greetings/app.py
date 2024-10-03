from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, json
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return redirect("/welcome", code = 302)

@app.route('/welcome')
def welcome():
    agent_id = request.headers.get('User-Agent')
    return render_template("index.html", agent_id=agent_id)

#route for challenge page        
@app.route('/VTJWamNtVjBJR0ZuWlc1MElEQXdOdz09')
def agent_authorized_or_not():
    #fetching the current user agent
    agent_id = request.headers.get('User-Agent')

    #array for all the possible user-agent substrings

    #processing the current user agent
    checking_authorization = agent_id.find("Mozilla")

    #taking decision based on the above process result
    if checking_authorization >= 0:
        return redirect("index.html", code = 302)
    else:
        return render_template("VTJWamNtVjBJR0ZuWlc1MElEQXdOdz09.html", title = 'Your are Authorized. Agent 007')

#route for flag
@app.route('/845y83hg387yt83', methods=['POST'])
def flag():
    return render_template("845y83hg387yt83.html", title = 'Flag')

if __name__ == '__main__':
   app.run()