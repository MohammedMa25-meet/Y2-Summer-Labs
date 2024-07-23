from flask import Flask, render_template, request, redirect, url_for, session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

firebaseConfig = {
  "apiKey": "AIzaSyCXXjV-WGS82-H2HC3zlJEs2TbkI3NjBNc",
  "authDomain": "movie-review-web.firebaseapp.com",
  "projectId": "movie-review-web",
  "storageBucket": "movie-review-web.appspot.com",
  "messagingSenderId": "916600957801",
  "appId": "1:916600957801:web:e4af6beb72be5791e6ebf8",
  "measurementId": "G-9MCDFMV49K",
  "databaseURL":"https://movie-review-web-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route('/')
def main():
    return redirect('/signup')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
	if request.method == 'POST':
	    email = request.form['email']
	    password = request.form['password']
	    name = request.form['name']
	    try:
	        
	        login_session['user'] = auth.create_user_with_email_and_password(email, password)
	        db.child("users").push({"name": name, "email": email})
	        return redirect(url_for('home'))
	    except Exception as e:
	        print(e)
	        print("error try again failed signup")
	        return render_template('signup.html',error="failed signup")
	else:
		return render_template('signup.html')
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user']= auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except Exception as e:
            print(e)
            print("error try again later")
            return render_template('/login',error="failed login ")
            
    else:
        return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/movies')
def movies():
    return render_template('movies.html')

if __name__ == '__main__':
    app.run(debug=True)


