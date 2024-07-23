from flask import Flask, render_template, request, redirect, url_for, session as login_session
import pyrebase

app = Flask(__name__)
app.secret_key = 'your-secret-key'

firebase_config = {
  "apiKey": "AIzaSyCqFScmacfZa2APBpwjY3BLCKzXVjhUh4M",
  "authDomain": "authentication-lab-30fe8.firebaseapp.com",
  "projectId": "authentication-lab-30fe8",
  "storageBucket": "authentication-lab-30fe8.appspot.com",
  "messagingSenderId": "303814170956",
  "appId": "1:303814170956:web:e74dcc88deb26a739157e9",
  "measurementId": "G-4EZJZCSEPM",
    "databaseURL": "https://authentication-lab-30fe8-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

@app.route('/')
def index():
    if 'user' in login_session:
        user_id = login_session['user']['localId']
        user_data = db.child("users").child(user_id).get().val()
        all_users = db.child("users").get().val()
        return render_template('home.html', user=user_data, all_users=all_users)
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        fav_movie = request.form['fav_movie']
        fav_song = request.form['fav_song']

        try:
            user = auth.create_user_with_email_and_password(email, password)
            user_id = user['localId']
            db.child("users").child(user_id).set({
                "name": name,
                "fav_movie": fav_movie,
                "fav_song": fav_song
            })
            login_session['user'] = user
            return redirect(url_for('index'))
        except Exception as e:
            error_message = str(e)
            print(f"Error: {error_message}")
            if "EMAIL_EXISTS" in error_message:
                return "The email address is already in use by another account."
            elif "INVALID_EMAIL" in error_message:
                return "The email address is not valid."
            elif "WEAK_PASSWORD" in error_message:
                return "The password is too weak."
            elif "MISSING_PASSWORD" in error_message:
                return "The password is missing."
            else:
                return "Failed to create account. Please check your details and try again."
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            login_session['user'] = user
            return redirect(url_for('index'))
        except Exception as e:
            error_message = str(e)
            print(f"Error: {error_message}")
            return "Failed to login. Check your credentials."
    return render_template('signin.html')

@app.route('/logout')
def logout():
    login_session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
