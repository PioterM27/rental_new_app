from rental_car_app import db

from datetime import datetime, date, timedelta

from flask import current_app

from werkzeug.security import generate_password_hash, check_password_hash


class Cars(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    production_year = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(50), nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    gearbox = db.Column(db.String(50), nullable=False)
    customer = db.relationship("Customer", back_populates="cars", secondary="rents")
    prices = db.relationship('Price', uselist=False, backref="cars")



    def to_json(self):
        author_to_json = {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "production_year": self.production_year,
            "photo": self.photo,
            "seats": self.seats,
            "gearbox": self.gearbox,
            "prices_low":self.prices.low_price,
            "prices_medium": self.prices.medium_price,
            "prices_high": self.prices.high_price,


        }
        return author_to_json
