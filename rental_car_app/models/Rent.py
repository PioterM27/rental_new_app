from rental_car_app import db


class Rent(db.Model):
    __tablename__ = "rents"
    car_id = db.Column(db.Integer, db.ForeignKey("cars.id"), primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    pickUp_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=False)

    def to_json(self):
        rents_to_json = {
            "car_id": self.car_id,
            "customer_id": self.customer_id,
            "price": self.price,
            "pickUp_date": self.pickUp_date.date(),
            "return_date": self.return_date.date(),
        }
        return rents_to_json
