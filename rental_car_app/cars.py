from flask import jsonify, render_template, request, url_for, redirect
import json
from flask_wtf import FlaskForm

from rental_car_app import app
from rental_car_app.models.Cars import Cars
from rental_car_app.models.Rent import Rent
from rental_car_app.models.Customer import Customer
from rental_car_app import db

from rental_car_app.Forms.SearchDate import SearchDate
from rental_car_app.Forms.CustomerData import CustomerData


@app.route("/first", methods=["GET", "POST"])
def main_page():
    return render_template("first_page.html")


@app.route("/", methods=["GET", "POST"])
def get_cars():
    cars = Cars.query
    forms2 = SearchDate()
    data_list = []
    formList = []
    for car in cars:
        formList.append(car.to_json())

    if request.method == "GET":
        return render_template(
            "get_cars_template.html", form1=forms2, current_picture="cars.jpg"
        )
    elif request.method == "POST":
        if request.form.get("rent-from") != None and request.form.get("rent-to") != None:
            data_list.append(request.form.get("rent-from"))
            data_list.append(request.form.get("rent-to"))
            return render_template(
                "get_cars_template.html",
                form1=forms2,
                form=formList,
                calendar=data_list,
                current_picture="cars.jpg",
            )
        elif request.form.get("name") != None:
            result = request
            requests = result.values
            index = int(requests.get("id")) - 1
            return render_template(
                "get_cars_template.html",
                form1=forms2,
                form=formList,
                current_picture=formList[index]["photo"],
                datas=formList[index],
                calendar=data_list
            )


@app.route("/reservation/<int:car_id>", methods=["GET", "POST"])
def get_reservation(car_id=None):
    test = request.values
    form = CustomerData()
    customer = Customer()
    if request.method == "GET":
        return render_template(
            "reservation.html",
            form=form,
            car_id=car_id,
            current_picture=test.get("photo"),
        )
    elif request.method == "POST":
        customer.first_name = request.form.get("first_name")
        customer.last_name = request.form.get("last_name")
        customer.email = request.form.get("email")
        customer.city = request.form.get("city")
        customer.state = "Poland"
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for("succes_forms"))

    return render_template(
        "reservation.html", form=form, current_picture=test.get("photo")
    )


@app.route("/succes/", methods=["POST"])
def succes_forms():
    print(request.form)
    return render_template("base.html")

