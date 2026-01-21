from flask import Flask, render_template
import requests
from blog import PostContainer
import os
from dotenv import load_dotenv

load_dotenv()

post_saver = []

website = os.getenv('website')

response = requests.get(website)
posts = response.json()


for post in posts:
    container = PostContainer(post_id=post["id"], title=post["title"], subtitle=post["subtitle"], body=post["body"], image_url=post["image_url"])
    post_saver.append(container)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs=post_saver)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:num>')
def post(num):
    blog_post = None
    for each_post in post_saver:
        if num == each_post.id:
            blog_post = each_post
    return render_template("post.html", new_post=blog_post)

if __name__ == "__main__":
    app.run(debug=True)