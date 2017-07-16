from flask import Flask 
from flask import request

app = Flask(__name__)

@app.route('/')
def index(name='Ted'):
	name = request.args.get('name', name)
	return "Hello it's {}!".format(name)


app.run(debug=True) 