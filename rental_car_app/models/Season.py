from rental_car_app import db


class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    season_names = db.Column(db.Integer, nullable=False)
    season_from = db.Column(db.Integer, nullable=False)
    season_to = db.Column(db.Integer, nullable=False)
