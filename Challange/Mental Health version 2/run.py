from flask import Flask, render_template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ILOVEYOU3000'

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	confirmusername = StringField('Confirm Username', validators=[DataRequired(), Length(min=2, max=20)])
	password = PasswordField('Password', validators=[DataRequired()])
	confirmpassword = PasswordField('Confirm Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Register')

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/depression")
def depression():
	return render_template("depression.html")

@app.route("/anxiety")
def anxiety():
	return render_template("anxiety.html")


@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', form = form)

@app.route("/register")
def register():
	form = RegisterForm()
	return render_template('register.html', form = form)


if __name__ == "__main__":
    app.run(debug=True)