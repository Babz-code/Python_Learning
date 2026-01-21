from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import random
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


#CREATE FORM
class NewPost(FlaskForm):
    title = StringField(label='Blog Post Tile', validators=[DataRequired()])
    subtitle = StringField(label='Blog Subtitle', validators=[DataRequired()])
    author = StringField(label='Your Name', validators=[DataRequired()])
    img_url = StringField(label='Blog Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField(label='Blog Content', validators=[DataRequired()])
    submit = SubmitField(label='Create Blog')

# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date,
            "body": self.body,
            "author": self.author,
            "img_url": self.img_url,
            "subtitle": self.subtitle
        }

with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.

    with app.app_context():
        all_blog = db.session.execute(db.select(BlogPost)).scalars().all()
        posts = [blog for blog in all_blog]
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/show-post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    with app.app_context():
        requested_post = db.session.get(BlogPost, post_id)

    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    new_blog_post = NewPost()
    if new_blog_post.validate_on_submit():
        new_blog = BlogPost(
            title=new_blog_post.title.data,
            date=date.today().strftime("%B %d, %Y"),
            subtitle = new_blog_post.subtitle.data,
            author = new_blog_post.author.data,
            img_url = new_blog_post.img_url.data,
            body = new_blog_post.body.data
        )
        with app.app_context():
            db.session.add(new_blog)
            db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', create_new_post=new_blog_post, mode='create')

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post_to_be_edited = db.session.get(BlogPost, post_id)
    new_blog_post = NewPost(obj=post_to_be_edited)
    if new_blog_post.validate_on_submit():
        new_blog_post.populate_obj(post_to_be_edited)
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))

    return render_template('make-post.html', create_new_post=new_blog_post, mode='edit')

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<post_id>')
def delete_post(post_id):
    post_to_be_deleted = db.session.get(BlogPost, post_id)
    db.session.delete(post_to_be_deleted)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
