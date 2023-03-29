import os
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Boolean, nullable=False, default=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_status")
def get_status():
    item = Item.query.get(1)
    return jsonify({'status' : item.status})

@app.route("/change_status")
def change_status():
    item = Item.query.get(1)
    item.status = not item.status
    db.session.commit()
    return jsonify({'status' : item.status})

if __name__ == "__main__":
    app.run(debug=True)