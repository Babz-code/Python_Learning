from flask import Flask
import random

random_num = random.randint(0, 9)

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='giphy'>"

@app.route("/<number>")
def number_guess(number):
    if int(number) < random_num:
        return "<h1 style=color:red>Too low, Try again</h1><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif int(number) > random_num:
        return "<h1 style=color:orange>Too high, Try again</h1><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style=color:green>Correct</h1><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"




app.run()