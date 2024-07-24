from flask import Flask, render_template, request, redirect, url_for, session as login_session
import pyrebase
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

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
            user = auth.create_user_with_email_and_password(email, password)
            login_session['user'] = user
            db.child("users").child(user['localId']).set({"name": name, "email": email})
            return redirect(url_for('home'))
        except Exception as e:
            print(e)
            return render_template('signup.html', error="Failed signup, try again.")
    else:
        return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            login_session['user'] = user
            return redirect(url_for('home'))
        except Exception as e:
            print(e)
            return render_template('login.html', error="Failed login, try again.")
    else:
        return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        user_id = login_session['user']['localId']
        user_info = db.child("users").child(user_id).get().val()
        name = user_info['name']

        review_text = request.form['review']
        file = request.files['poster']

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            db.child("reviews").push({
                "user_id": user_id,
                "user_name": name,
                "review_text": review_text,
                "poster_url": url_for('static', filename='uploads/' + filename)
            })
            return redirect(url_for('movies'))
    return render_template('review.html')

@app.route('/movies')
def movies():
    reviews = db.child("reviews").get().val()
    return render_template('movies.html', reviews=reviews)

if __name__ == '__main__':
    app.run(debug=True)
