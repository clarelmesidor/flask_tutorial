from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello! this is the main page <h1>Hello<h1>"

app.run(host='0.0.0.0', port= 5000)