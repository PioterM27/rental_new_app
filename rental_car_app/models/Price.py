from rental_car_app import db


class Price(db.Model):
    __tablename__ = "prices"
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(255), nullable=False)
    high_price = db.Column(db.Integer, nullable=False)
    medium_price = db.Column(db.Integer, nullable=False)
    low_price = db.Column(db.Integer, nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=True)

