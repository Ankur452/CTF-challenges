from flask import Flask, render_template

# Create a Flask web application
app = Flask(__name__)

# Define a route and a function to handle requests to the root URL ("/")
@app.route("/")
def home():
    return render_template("index.html")

# Run the application if this script is executed
if __name__ == "__main__":
    app.run(debug=True)
