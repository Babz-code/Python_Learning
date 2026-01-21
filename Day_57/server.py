from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    #To get age
    response = requests.get(f"https://api.agify.io?name={name}")
    age = response.json()["age"]

    #To get gender
    response = requests.get(f"https://api.genderize.io?name={name}")
    gender = response.json()["gender"]
    return render_template("index_0.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)
