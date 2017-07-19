import json
from flask import (Flask, render_template, request, redirect,
				  url_for, make_response)


app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/index', methods=['GET'])
def back():
	return redirect(url_for('index'))

@app.route('/save', methods=['POST'])
def save():
	name = request.form['name']
	return render_template("save.html", name=name)
	
	





app.run(debug=True) 


# @app.route('/add/<float:num1>/<float:num2>')
# @app.route('/add/<int:num1>/<int:num2>')
# @app.route('/add/<int:num1>/<float:num2>')
# @app.route('/add/<float:num1>/<int:num2>')
# def add(num1, num2):
# 	return render_template("add.html", num1=num1, num2=num2)