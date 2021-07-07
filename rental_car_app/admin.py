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
from rental_car_app.Forms.LoginForm import LoginForm
from rental_car_app.Forms.RegistrationForm import RegistrationForm


@app.route("/admin", methods=["GET", "POST"])
def admin_panel():
    cars = Cars.query
    formList = []
    for car in cars:
        formList.append(car.to_json())
    return render_template("admin_view.html", car_form=formList)
