from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = "password"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        birth_month = request.form['birth_month']
        session['name'] = name
        session['birth_month'] = birth_month
        num_letters = len(birth_month)
        fortune_list = ["money", "intelligence", "good sleep", "relaxed", "gold", "silver", "diamond", "sapphire", "bronze", "iron"]
        if num_letters == 0:
            session['fortune'] = "no fortune"
        else:
            fortune_index = num_letters % len(fortune_list)
            session['fortune'] = fortune_list[fortune_index]       
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    if 'name' in session:
        name = session['name']
        return render_template("hello.html", name=name)
    return redirect(url_for('login'))

@app.route('/fortune')
def fortune():
    if 'fortune' in session:
        birth_month = session['birth_month']
        fortune = session['fortune']
        return render_template("fortune.html", birth_month=birth_month, fortune=fortune)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)










