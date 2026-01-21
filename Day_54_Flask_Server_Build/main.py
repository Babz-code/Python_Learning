from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/toyo")
def intro():
    return "<h1>This is Me</h1>"

# Created my own python decorator
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s Blog post")

new_user = User("Toyosi")
new_user.is_logged_in = True
create_blog_post(new_user)