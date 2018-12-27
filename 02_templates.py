from flask import Flask, render_template

app = Flask(__name__)

## Dummy data to show on home page
oldBlogs =[
			{'author': 'Author self',
			 'date'  : '27 Dec 2018',
			 'Topic' : 'Introduction',
			 'Text'  : 'Introduction to oneself is a great medium to self discovery.'
			},
			{'author': 'Author followed 1',
			 'date'  : '27 Dec 2018',
			 'Topic' : 'Daily',
			 'Text'  : 'Wake up, dress up and show up !'
			},
			{'author': 'Author followed 2',
			 'date'  : '27 Dec 2018',
			 'Topic' : 'Goals',
			 'Text'  : 'Efforts without a goal is similar to wandering aimlessly. You walk a lot but don\'t go anywhere.'
			}
]

@app.route('/')
@app.route('/home')
def home():
	return render_template("home.html",blogStream=oldBlogs, iTitle='UBlog.com')

@app.route('/about')
def about():
	return render_template("about.html", blogCount=len(oldBlogs))

if __name__ == "__main__":
	app.run(debug=True)