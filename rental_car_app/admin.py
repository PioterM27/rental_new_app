from flask import (
    abort,
    jsonify,
    request,
    render_template,
    request,
    url_for,
    redirect,
    session,
)
from flask_login import login_required, login_user, logout_user, current_user

from rental_car_app import db, app
from rental_car_app.models.Cars import Cars
from rental_car_app.models.Rent import Rent
from rental_car_app.Forms.LoginForm import LoginForm
from rental_car_app.Forms.RegistrationForm import RegistrationForm


@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin_panel():
    cars = Cars.query
    rents = Rent.query
    formList = []
    rentList = []
    for car in cars:
        formList.append(car.to_json())
    for rent in rents:
        rentList.append(rent.to_json())
    return render_template("admin_view.html", car_form=formList, rents_form=rentList)
