from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

texts = ["Lorem ipsum dolor, sit amet consectetur adipisicing elit. Velit vitae non sit consectetur, similique eaque, harum ipsa dignissimos id facere nostrum aliquam repellat corrupti in ducimus accusantium ex dolore! Aliquid?"]

@app.route("/one")
def one():
    return texts[0]

@app.route("/two")
def two():
    return texts[1]

@app.route("/three")
def three():
    return texts[2]

if __name__ == '__main__':
    app.run(debug=True)