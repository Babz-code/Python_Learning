from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
# from db import Books


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

#Database setup with flask
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

db.init_app(app)
class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    author: Mapped[str] = mapped_column(String(250))
    rating: Mapped[float]



@app.route('/')
def home():
    all_books = []
    # To Read from Database
    with app.app_context():
        result = db.session.execute(db.select(Books).order_by(Books.id))
        all_data = result.scalars()
        for data in all_data:
            formatted_data = {
                "id": data.id,
                "title": data.title,
                "author": data.author,
                "rating": data.rating
            }
            all_books.append(formatted_data)
    return render_template('index.html', books=all_books)


@app.route("/add",  methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('name')
        author =  request.form.get('author')
        rating = request.form.get('rating')

        # Create new entries to Database
        with app.app_context():
            new_book = Books(title=title, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template('add.html')


@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    edit_books = db.get_or_404(Books, id)

    if request.method == "POST":
        new_rating = request.form.get('rating')
        print(new_rating)

        with app.app_context():
            book_to_update = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
            # or book_to_update = db.get_or_404(Book, book_id)
            book_to_update.rating = new_rating
            db.session.commit()
        return redirect(url_for("home"))
    return render_template('edit.html', user_data=edit_books)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

