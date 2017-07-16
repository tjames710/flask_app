from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello there it's my first flask app!"


app.run(debug=True) #teamtreehouse uses port 8000 and host is 0.0.0.0