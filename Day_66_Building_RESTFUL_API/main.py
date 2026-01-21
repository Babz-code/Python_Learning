from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random



app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "has_sockets": self.has_sockets,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "can_take_calls": self.can_take_calls,
            "seats": self.seats,
            "coffee_price": self.coffee_price
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/get_all')
def get_all():
    with app.app_context():
        all_cafes = db.session.execute(db.select(Cafe)).scalars().all()

    return jsonify(all_cafe_dict=[cafe.to_dict()for cafe in all_cafes])


@app.route("/random")
def get_random_cafe():
    with app.app_context():
        all_cafes = []
        cafes = db.session.execute(db.select(Cafe)).scalars().all()
        random_cafe = random.choice(cafes)
    return jsonify(dict_cafe = random_cafe.to_dict())

@app.route("/search")
def search_for_cafe():
    loc = request.args.get("loc").capitalize()

    with app.app_context():
        cafe_to_search = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()

        if cafe_to_search:
            return jsonify(searched_cafe=[cafe.to_dict() for cafe in cafe_to_search])
        else:
            return jsonify(error={'Not Found': "Sorry! your search didn't return any variable"})


# HTTP POST - Create Record
@app.route('/add_cafe', methods=['POST'])
def add_cafe():
    with app.app_context():
        new_entry = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price")
        )
        db.session.add(new_entry)
        db.session.commit()
    return jsonify(
        {"response":
             {"success": "Successfully added cafe"}
         }
    )


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe_to_be_updated = db.session.get(Cafe, cafe_id)

    if cafe_to_be_updated is None:
        return jsonify(error={"Not Found": "A cafe with that id was not found"}), 404

    cafe_to_be_updated.coffee_price = new_price
    db.session.commit()
    return jsonify({"success": "Successfully updated the price"}), 200

# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    access_key = request.args.get("api_key")

    if access_key == "TopSecretAPIKey":
        cafe_to_be_deleted = db.session.get(Cafe, cafe_id)

        if cafe_to_be_deleted is None:
            return jsonify(error={"Not Found": "Sorry! The cafe with that id doesn't exist"}), 404

        db.session.delete(cafe_to_be_deleted)
        db.session.commit()
        return jsonify({"success": "Cafe was deleted successfully"}), 200
    else:
        return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct Api key"}), 403


if __name__ == '__main__':
    app.run(debug=True)

#https://documenter.getpostman.com/view/51397028/2sBXVfjrwh
# My publish link