from flask import Flask
app = Flask(__name__)

@app.route("/")
def testFlask():
	return "<h1><center>Hello Flask !!</center></h1>"
	
if __name__ == "__main__":
	app.run(debug=True)