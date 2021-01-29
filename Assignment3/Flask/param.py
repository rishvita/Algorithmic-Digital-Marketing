from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
all_posts=[
{
	'title':'Post 1',
	'content':'This is content of post 1',
	'author' : 'Prana'
},
{
	'title':'Post 2',
	'content':'This is content of post 2'
}
]


@app.route('/second')
def secondpage():
    return "This is my second page!"

@app.route('/onlyget',methods=['GET'])
def onlyget():
    return "This can only get this webpage!"

@app.route('/posts')
def posts():
	return render_template('posts.html',posts=all_posts)


    
@app.route('/method',methods =['GET','POST'])
def method():
    if request.method == 'POST':
        return "It is a post request"
    else:
        return "It is get request"

app.run()