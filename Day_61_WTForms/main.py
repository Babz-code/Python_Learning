from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
import os
from dotenv import load_dotenv
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['BOOTSTRAP_BTN_STYLE'] = 'dark'

bootstrap = Bootstrap5(app)

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        user_email = form.email.data
        user_pw = form.password.data
        if user_email == "admin@email.com" and user_pw == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")


    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

