import json
from flask import (Flask, render_template, request, redirect,
				  url_for, make_response)


app = Flask(__name__)

def get_saved_data():
	try:
		data = json.loads(request.cookies.get('character'))
	except TypeError:
		data = {}
	return data	

@app.route('/')
def index():
	data = get_saved_data()
	return render_template("index.html", saves=data)

@app.route('/save', methods=['POST'])
def save():
	response = make_response(redirect(url_for('index')))
	data = get_saved_data()
	data.update(dict(request.form.items()))
	response.set_cookie('character', json.dumps(data))
	return response
	
	





app.run(debug=True) 


# @app.route('/add/<float:num1>/<float:num2>')
# @app.route('/add/<int:num1>/<int:num2>')
# @app.route('/add/<int:num1>/<float:num2>')
# @app.route('/add/<float:num1>/<int:num2>')
# def add(num1, num2):
# 	return render_template("add.html", num1=num1, num2=num2)