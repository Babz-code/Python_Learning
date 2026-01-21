from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length
import requests
from dotenv import load_dotenv
import os

load_dotenv()



class AddMovieForm(FlaskForm):
    movie_title = StringField(label='Your Movie Title', validators=[DataRequired(message='Please enter a movie name')])
    submit = SubmitField(label='Search')

