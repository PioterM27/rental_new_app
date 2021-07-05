from rental_car_app import db


class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False, index=True)
    last_name = db.Column(db.String(255), nullable=False, index=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    city = db.Column(db.String(255), nullable=False, index=True)
    state = db.Column(db.String(255), nullable=False, index=True)
    car_id = db.Column(db.Integer,nullable=False)
    cars = db.relationship("Cars", back_populates="customer", secondary="rents")
