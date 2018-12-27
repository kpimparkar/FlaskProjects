from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def testFlask():
	return "<h1><center>Hello Flask !!</center></h1>"
	
@app.route("/aboutus")
def aboutus():
	return """<h1><center>About us</center></h1>
			  <p><center>This is a basic web app created using flask framework</center></p>"""
	
if __name__ == "__main__":
	app.run(debug=True)