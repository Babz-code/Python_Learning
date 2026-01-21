from flask import Flask, render_template, url_for
import requests
from post import PostContainer
import os
from dotenv import load_dotenv

load_dotenv()

post_content = []

website = os.getenv('website')
response = requests.get(website)
posts = response.json()
for post in posts:
    container = PostContainer(post_id=post["id"], title=post["title"], subtitle=post["subtitle"], body=post["body"])
    post_content.append(container)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs=post_content)

@app.route('/blog/<int:num>')
def blog(num):
    blog_post = None
    for each_post in post_content:
        if each_post.id == num:
            blog_post = each_post
    return render_template("post.html", blog=blog_post)

if __name__ == "__main__":
    app.run(debug=True)
