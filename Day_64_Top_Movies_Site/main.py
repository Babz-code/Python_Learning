from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length
from form import AddMovieForm
import os
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap5(app)

# TODO CREATE WTFORM FOR REVIEW & RATING UPDATE
class RatingForm(FlaskForm):
    update_rating = FloatField(label='Your Rating (out of 10)')
    update_review = StringField(label='Your New Review', validators=[Length(max=250)])
    submit = SubmitField(label='Done')

# CREATE DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies-collection.db"

#Database setup with flask
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

db.init_app(app)
class Movies(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    year: Mapped[int]
    description: Mapped[str] = mapped_column(Text)
    rating: Mapped[float]
    ranking: Mapped[int]
    review: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(250))

# TODO CREATE TABLE
# with app.app_context():
#     db.create_all()

@app.route("/add", methods=["GET", "POST"])
def add():
    #Importing our form
    add_movie_form = AddMovieForm()

    if add_movie_form.validate_on_submit():
        movie_to_add = add_movie_form.movie_title.data

        #Use query to pull data fro TheMovieDatabase
        url = os.getenv("API_LINK")
        headers = {
            "accept": "application/json",
            "Authorization": f'Bearer {os.getenv("ACCESS_TOKEN")}'
        }
        parameters = {
            "query": movie_to_add
        }

        response = requests.get(url, params=parameters, headers=headers)
        returned_data = response.json()['results']

        return render_template('select.html', data=returned_data)

    return render_template('add.html', movie_form=add_movie_form)

@app.route("/")
def home():
    list_of_movies = []

    with app.app_context():
        result = db.session.execute(db.select(Movies).order_by(Movies.rating.desc()))
        all_movies = result.scalars()
        for index, movie in enumerate(all_movies, start=1):
            formatted_movies = {
                "id": movie.id,
                "title": movie.title,
                "year": movie.year,
                "description": movie.description,
                "rating": movie.rating,
                "ranking": index,
                "review": movie.review,
                "img_url": movie.img_url
            }
            list_of_movies.append(formatted_movies)

    return render_template("index.html", movies_db=list_of_movies)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    current_movie = db.get_or_404(Movies, id)

    #Import our WTForm
    form = RatingForm()
    if form.validate_on_submit():
        new_rating = form.update_rating.data
        new_review = form.update_review.data

        with app.app_context():
            movie_to_update = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar()
            movie_to_update.rating = new_rating
            movie_to_update.review = new_review
            db.session.commit()
        return redirect(url_for("home"))

    return render_template('edit.html', form=form, movie_edit=current_movie)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for("home"))

@app.route('/get/<int:id>', methods=['GET', 'POST'])
def get(id):
    movie_id = id
    details_url = f'{os.getenv("GET_DETAILS_APN")}/{movie_id}'
    headers = {
        "accept": "application/json",
        "Authorization": f'Bearer {os.getenv("ACCESS_TOKEN")}'
    }
    response = requests.get(details_url, headers=headers)
    data = response.json()

    # TODO Add to the Database
    with app.app_context():
        new_movie = Movies(
        title=data['title'],
        year=data['release_date'].split('-')[0],
        description=data['overview'],
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
        rating=0,
        ranking=0,
        review=""
        )
        db.session.add(new_movie)
        db.session.commit()

        # TODO To give new movie added to database it's rating and review
        movie_added_title = data['title']
        get_movie_added = db.session.execute(db.select(Movies).where(Movies.title == movie_added_title)).scalar()
        movie_added_id = get_movie_added.id

    return redirect(url_for("update", id=movie_added_id))


if __name__ == '__main__':
    app.run(debug=True)

# rating=7.3,
# ranking=9,
# review="I liked the water.",