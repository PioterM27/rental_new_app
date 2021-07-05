from rental_car_app import db


class Rent(db.Model):
    __tablename__ = "rents"
    car_id = db.Column(db.Integer, db.ForeignKey("cars.id"), primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    pickUp_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=False)
