from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
	return render_template("index.html")


@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
	return render_template("add.html", num1=num1, num2=num2)


@app.route('/save', methods=['POST'])
def save():
	name = request.form['name']
	return render_template("save.html", name=name)
	
	





app.run(debug=True) 