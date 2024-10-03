from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, json
import codecs

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return redirect("/welcome", code = 302)

@app.route('/welcome')
def welcome():
    agent_id = request.headers.get('User-Agent')
    return render_template("index.html", agent_id=agent_id)

#route for challenge page        
@app.route('/vbmvdgh9eruihag934yg9', methods=['POST','GET'])
def agent_authorized_or_not():
    #fetching the current user agent
    agent_id = request.headers.get('User-Agent')

    #array for all the possible user-agent substrings
    user_agents = ['Mozilla','Roku','Dalvik','Apple']

    #processing the current user agent
    checking_authorization = agent_id.find("Mozilla")

    #taking decision based on the above process result
    if checking_authorization >= 0:
        return redirect("/welcome", code = 302)
    else:
        return redirect("/fuytr76r65e75d8yfg89h08g8f8if6", code = 302)

#route for flag
@app.route('/fuytr76r65e75d8yfg89h08g8f8if6')
def challenge():
    agent_id = request.headers.get('User-Agent')

    # Function to translate plain text to ROT13
    encrypted_message = codecs.encode("Use the '/845y83hg387yt83' route to get to the flag", 'rot_13')
       
    return render_template("VTJWamNtVjBJR0ZuWlc1MEl123EQXdOdz09.html", encrypted_message=encrypted_message, title = "Your are Authorized. Agent 007")

#route for flag
@app.route('/845y83hg387yt83')
def flag():
    return render_template("845y83hg387yt83.html", title = 'Flag')

if __name__ == '__main__':
   app.run()

