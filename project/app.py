from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


Config = {

  "apiKey": "AIzaSyA4oKRP03CW_hUUb4PvLgArywJ6rat6z9E",

  "authDomain": "personal-project-y2.firebaseapp.com",

  "projectId": "personal-project-y2",

  "storageBucket": "personal-project-y2.appspot.com",

  "messagingSenderId": "639819640975",

  "appId": "1:639819640975:web:b4cbe45b01b3be18f600fa",

  "measurementId": "G-NKEP284JSN",

  "databaseURL":"https://personal-project-y2-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def login():
	if request.method=='POST':
		email = request.form['email']
		password = request.form['password']
		try:
			login_session["user"]= auth.sign_in_with_email_and_password(email,password)
		except:
			print("error")
	return render_template('login.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
	if request.method=='POST':
		username= request.form['username']
		email = request.form['email']
		password = request.form['password']
		try:
			login_session["user"]= auth.create_user_with_email_and_password(email,password)
			user = {"username":username,"password":password,"email":email}
			db.child("Users").child(login_session['user']['localId']).set(user)
		except:
			print("error")
	return render_template('signup.html')


if __name__=='__main__':
	app.run(debug=True)