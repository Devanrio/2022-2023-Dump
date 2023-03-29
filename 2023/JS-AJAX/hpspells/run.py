from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/")
def index() :
    return render_template("index.html")

@app.route("/characters")
def characters():
    return render_template("characters.html")

@app.route("/characters/gryffindor")
def gryffindor():
    return render_template("gryffindor.html")

@app.route("/characters/ravenclaw")
def ravenclaw():
    return render_template("ravenclaw.html")

@app.route("/characters/hufflepuff")
def hufflepuff():
    return render_template("hufflepuff.html")

@app.route("/characters/slytherin")
def slytherin():
    return render_template("slytherin.html")

@app.route("/spells")
def spells():
    return render_template("spells.html")


#API GATEAWAY
@app.route("/api/currency/latest")
def api_currency_latest() :
    try :
        with open("spells.json") as file :
            data = json.load(file)
    except :
        return jsonify({
            "status" : False
        })
    else :
        response = jsonify(data)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return jsonify(data)

app.run(debug=True)