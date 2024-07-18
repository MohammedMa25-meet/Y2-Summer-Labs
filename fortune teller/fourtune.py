from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("hello.html")

@app.route('/fortune')
def fortune():
    num = random.randint(0, 9)
    fortune_list = ["money", "intelligence", "good sleep", "relaxed", "gold", "silver", "diamond", "sapphire", "bronze", "iron"]
    the_random = fortune_list[num]
    return render_template("fortune.html", fortune=the_random)

if __name__ == '__main__':
    app.run(debug=True)

