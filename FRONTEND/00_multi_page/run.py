from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/one")
def one():
    return render_template("one.html")

@app.route("/two")
def two():
    return render_template("two.html")

@app.route("/three")
def three():
    return render_template("three.html")

if __name__== '__main__':
    app.run(debug=True)