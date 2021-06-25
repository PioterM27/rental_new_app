from rental_car_app import db


class Rent(db.Model):
    __tablename__ = "rent"
    car_id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    pickUp_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=False)
