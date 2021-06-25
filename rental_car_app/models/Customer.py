from rental_car_app import db


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False, unique=True, index=True)
    last_name = db.Column(db.String(255), nullable=False, unique=True, index=True)
    email = db.Column(db.String(255), nullable=False, unique=True)

