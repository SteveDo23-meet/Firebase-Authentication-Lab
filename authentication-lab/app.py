from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


firebaseConfig = {
  "apiKey": "AIzaSyBK31Rb887yZDPtfGxSFaWUIsOsnAuXQIQ",
  "authDomain": "tonal-shore-325713.firebaseapp.com",
  "projectId": "tonal-shore-325713",
  "storageBucket": "tonal-shore-325713.appspot.com",
  "messagingSenderId": "862702764406",
  "appId": "1:862702764406:web:6e819b95149cd473f9fa57",
  "measurementId": "G-YRFB0KS86M"
  "databaseurl" : ""
}


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'post':
        email = request.form['email']
        password = request.form['password']
    try:
        login_session['user'] = 
            auth.sign_in_with_email_and_password(email , password)
        return redirect(url_for('home'))
    except :
        error = "Authentication failed"

return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'post':
        email = request.form['email']
        password = request.form['password']
    try:
        login_session['user'] = 
            auth.create_user_with_email_and_password(email , password)
        return redirect(url_for('add_tweet'))
    except :
        error = "Authentication failed"

return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


@app.route('/signout', methods=['GET', 'POST'])
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))

return render_template("signin.html")

if __name__ == '__main__':
    app.run(debug=True)

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = flask(__name__)