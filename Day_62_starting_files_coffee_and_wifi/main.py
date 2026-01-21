from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# app.config['BOOTSTRAP_BTN_STYLE'] = 'success'  # Green buttons by default
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'darkly'
bootstrap = Bootstrap4(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField(label='Find us on Google Map (URL)', validators=[DataRequired(), URL()])
    open_time = StringField(label='Opening Time e.g 7 a.m.', validators=[DataRequired()])
    close_time = StringField(label='Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField(
        label='Coffee Rating',
        choices=[(1, '☕️'), (2, '☕️☕️'), (3, '☕️☕️☕️'),
                 (4, '☕️☕️☕️☕️'), (5, '☕️☕️☕️☕️☕️')],
        coerce=int,
        validators=[DataRequired()])
    wifi_rating = SelectField(
        label='Wifi Rating',
        choices=[(1, '💪'), (2, '💪💪'), (3, '💪💪💪'),
                 (4, '💪💪💪💪'), (5, '💪💪💪💪💪')],
        coerce=int,
        validators=[DataRequired()])
    power_rating = SelectField(
        label='Power Rating',
        choices=[(1, '🔌'), (2, '🔌🔌'), (3, '🔌🔌🔌'),
                 (4, '🔌🔌🔌🔌'), (5, '🔌🔌🔌🔌🔌')],
        coerce=int,
        validators=[DataRequired()])
    submit = SubmitField('Submit')



def rating_to_emoji(rating, emoji):
    """Convert rating number to repeated emoji"""
    return emoji * rating


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=['GET', 'POST'] )
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = [
            form.cafe.data,
            form.location_url.data,
            form.open_time.data,
            form.close_time.data,
            rating_to_emoji(form.coffee_rating.data, '☕️'),
            rating_to_emoji(form.wifi_rating.data, '💪'),
            rating_to_emoji(form.power_rating.data, '🔌')
        ]

        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            new_csv = csv.writer(csv_file)
            new_csv.writerow(new_cafe)

        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', encoding='utf-8') as csv_file:
        csv_data = csv.DictReader(csv_file)
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
