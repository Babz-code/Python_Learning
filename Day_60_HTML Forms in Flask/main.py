from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

my_email = os.getenv("MY_EMAIL")
password = os.getenv("MY_PASSWORD")
blog_ep = os.getenv("MY_BLOG_EP")

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get(blog_ep).json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        full_message = f"Subject: New User \n\n{message}\nname: {name}\nemail: {email}"
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            # server.starttls()
            server.login(my_email, password)
            server.sendmail(my_email, my_email, full_message)
            print("Email sent successfully!")
            server.quit()
            return render_template("contact.html", passed=True)

        except Exception as e:
            print(f"Error: {e}")



    return render_template("contact.html", passed=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/form-entry", methods=["POST"])
def receive_data():
    return "Successfully sent your message"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
