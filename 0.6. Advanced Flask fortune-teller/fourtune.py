from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        birth_month = request.form['birth_month']
        return redirect(url_for('fortune', birth_month=birth_month))
    return render_template("hello.html")

@app.route('/fortune/<birth_month>')
def fortune(birth_month):
    num_letters = len(birth_month)
    fortune_list = ["money", "intelligence", "good sleep", "relaxed", "gold", "silver", "diamond", "sapphire", "bronze", "iron"]
    
    # Calculate index within the range of fortune_list
    if num_letters > len(fortune_list):
        fortune_index = num_letters % len(fortune_list)
    else:
        fortune_index = num_letters
    
    the_random = fortune_list[fortune_index]
    return render_template("fortune.html", birth_month=birth_month, fortune=the_random)

if __name__ == '__main__':
    app.run(debug=True)








