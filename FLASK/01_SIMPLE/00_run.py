from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world!"

@app.route("/anas")
def anas():
    returnn "Anas!"

@app.route("/html")
def more_html():
    return "<h1> Hello, Buddy! </h1>"

app.run(debug=True) #host="0.0.0.0", port="8000"