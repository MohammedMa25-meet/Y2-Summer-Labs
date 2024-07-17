from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return """
        <html>
        <body>
            <a href='/home'>Go to home page</a>
        </body>
        </html>
    """

@app.route('/home')
def home():
    return '''
        <html>
        <head><title>Photos</title></head>
        <body>
            <p>Welcome to a photo gallery consisting of food, pets, and outer space</p>
            <a href="/food1">Go to the first food photo</a>
            <br>
            <a href="/pet1">Go to the first pet photo</a>
        </body>
        </html>
    '''

@app.route('/food1')
def food1():
    return '''
        <html>
        <head><title>Food Photo 1</title></head>
        <body>
            <img src="https://promova.com/content/italian_food_words_26076fb3f5.png" alt="Food Photo 1" width="400">
            <br>
            <a href="/food2">Go to the next food photo</a>
            <br>
            <a href="/home">Go back to home</a>
        </body>
        </html>
    '''

@app.route('/food2')
def food2():
    return '''
        <html>
        <head><title>Food Photo 2</title></head>
        <body>
            <img src="https://images.immediate.co.uk/production/volatile/sites/30/2022/08/Corndogs-7832ef6.jpg?quality=90&resize=556,505" alt="Food Photo 2" width="400">
            <br>
            <a href="/food3">Go to the next food photo</a>
            <br>
            <a href="/food1">Go back to the first food photo</a>
        </body>
        </html>
    '''

@app.route('/food3')
def food3():
    return '''
        <html>
        <head><title>Food Photo 3</title></head>
        <body>
            <img src="https://www.eatingwell.com/thmb/m5xUzIOmhWSoXZnY-oZcO9SdArQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/article_291139_the-top-10-healthiest-foods-for-kids_-02-4b745e57928c4786a61b47d8ba920058.jpg" alt="Food Photo 3" width="400">
            <br>
            <a href="/food2">Go back to the second food photo</a>
            <br>
            <a href="/home">Go back to home</a>
        </body>
        </html>
    '''

@app.route('/pet1')
def pet1():
    return '''
        <html>
        <head><title>Pet Photo 1</title></head>
        <body>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvmOOBSFn1Y9Z101MXACWdA8QABuaKbG-cew&s" alt="Pet Photo 1" width="400">
            <br>
            <a href="/pet2">Go to the next pet photo</a>
            <br>
            <a href="/home">Go back to home</a>
        </body>
        </html>
    '''

@app.route('/pet2')
def pet2():
    return '''
        <html>
        <head><title>Pet Photo 2</title></head>
        <body>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQf56o1QNYsv-rZfMuSNIOJahgzaIqlPT1iKbHbyNYww5-zTPwyMLXjjHhhbqzQyoeUCdo&usqp=CAU" alt="Pet Photo 2" width="400">
            <br>
            <a href="/pet3">Go to the next pet photo</a>
            <br>
            <a href="/pet1">Go back to the first pet photo</a>
        </body>
        </html>
    '''

@app.route('/pet3')
def pet3():
    return '''
        <html>
        <head><title>Pet Photo 3</title></head>
        <body>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRq8_Jukp3K7b28_qvLhqBg6pSZDdWjjeWSaC4Orpl2FAvityBBjjBVN47YmPteQ7c4Os&usqp=CAU" alt="Pet Photo 3" width="400">
            <br>
            <a href="/pet2">Go back to the second pet photo</a>
            <br>
            <a href="/home">Go back to home</a>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

