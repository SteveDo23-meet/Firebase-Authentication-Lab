from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = {
  "apiKey": "AIzaSyBK31Rb887yZDPtfGxSFaWUIsOsnAuXQIQ",
  "authDomain": "tonal-shore-325713.firebaseapp.com",
  "projectId": "tonal-shore-325713",
  "storageBucket": "tonal-shore-325713.appspot.com",
  "messagingSenderId": "862702764406",
  "appId": "1:862702764406:web:6e819b95149cd473f9fa57",
  "measurementId": "G-YRFB0KS86M",
  "databaseURL" : "https://tonal-shore-325713-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user']=auth.sign_in_with_email_and_password(email , password)
            return redirect(url_for('home'))
        except :
            error = "Authentication failed"

    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        bio = request.form['bio']
        full_name = request.form['full_name']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email , password)
            user = {"username": username, "email": email , "password" : password , "bio" : bio , "full_name" : full_name}
            db.child("Users").child(login_session['user']['localId']).set(user)
            return redirect(url_for('add_tweet'))
        except :
            error = "Authentication failed"

    return render_template("signup.html")

tweets= db.child("Tweets").get().val()
@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    error = ""
    if request.method == 'POST':
        Title = request.form['Title']
        Text = request.form['Text']
        uid = login_session['user']['localId']
        tweet = {"Title" : Title , "Text" : Text , "uid" : uid}

        try:
            db.child("Tweets").push(tweet)
            return redirect(url_for("all_tweets"))
        except :
            error = "Could not add the tweet sorry"

    return render_template("add_tweet.html")

@app.route('/signout', methods=['GET', 'POST'])
def signout():
    try:
        login_session['user'] = None
        auth.current_user = None
        return redirect(url_for('signin'))
    except:    
        return render_template("signin.html")

@app.route('/all_tweets' , methods=['GET' , 'POST'])
def all_tweets():
    tweets = db.child('Tweets').get().val()
    return render_template('all_tweets.html' , Tweets = tweets)

if __name__ == '__main__':
    app.run(debug=True)


