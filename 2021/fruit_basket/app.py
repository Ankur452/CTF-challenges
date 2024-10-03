from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, json
import codecs

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return redirect("/welcome", code = 302)

@app.route('/welcome')
def welcome():
    return render_template("index.html")

#route for challenge page        
@app.route('/djshg8347hiudsfy78hffrlksdcnioehw89', methods=['POST','GET'])
def choice():
    if request.method == "POST":
        choice = request.form.get("choice").lower()
            
    if choice == "yes":
        return render_template("geoirhg34htgierighdeg438.html")

    else:
        return redirect("/welcome", code = 302)

@app.route('/usith7b37843b74wb473h5g', methods=['POST','GET'])
def checking_for_apples():
    if request.method == "POST":
        fruit_name = request.form.get("fruit_name").lower()
    
    if fruit_name == "apple":
        return render_template("74tyvb37vb4t3v98t54.html", title = 'Flag')
    
    else:
        return redirect("/welcome", code = 302)

# #route for flag
# @app.route('/74tyvb37vb4t3v98t54')
# def flag():
#     return render_template("74tyvb37vb4t3v98t54.html", title = 'Flag')

if __name__ == '__main__':
   app.run()

