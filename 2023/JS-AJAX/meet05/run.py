from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/")
def index() :
    return render_template("index.html")

#API GATEAWAY
@app.route("/api/currency/latest")
def api_currency_latest() :
    try :
        with open("data.json") as file :
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