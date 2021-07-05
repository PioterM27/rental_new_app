from flask import jsonify, render_template, request, url_for, redirect, session
import json
from flask_wtf import FlaskForm

from rental_car_app import app
from rental_car_app.models.Cars import Cars
from rental_car_app.models.Rent import Rent
from rental_car_app.models.Price import Price
from rental_car_app.models.Customer import Customer
from rental_car_app.Control.PriceCounter import PriceCounter
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
    # session['data']
    formList = []
    for car in cars:
        formList.append(car.to_json())

    if request.method == "GET":
        return render_template(
            "get_cars_template.html", form1=forms2, current_picture="cars.jpg"
        )
    elif request.method == "POST":
        if (
            request.form.get("rent-from") != None
            and request.form.get("rent-to") != None
        ):
            session["rent-from"] = request.form.get("rent-from")
            session["rent-to"] = request.form.get("rent-to")
            # data_list.append(request.form.get("rent-to"))
            return render_template(
                "get_cars_template.html",
                form1=forms2,
                form=formList,
                calendar=session,
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
                calendar=session,
            )


@app.route("/reservation/<int:car_id>", methods=["GET", "POST"])
def get_reservation(car_id=None):
    car_price = Price.query.filter(Price.car_id == car_id).one()
    test = request.values
    form = CustomerData()
    customer = Customer()
    price = PriceCounter(
        session.get("rent-from"), session.get("rent-to"), car_price.medium_price
    )
    session["price"] = price.count_price()
    if request.method == "GET":
        return render_template(
            "reservation.html",
            form=form,
            car_id=car_id,
            current_picture=test.get("photo"),
            calendar=session,
        )
    elif request.method == "POST":
        customer.first_name = request.form.get("first_name")
        customer.last_name = request.form.get("last_name")
        customer.email = request.form.get("email")
        customer.city = request.form.get("city")
        customer.state = "Poland"
        customer.car_id = car_id
        db.session.add(customer)
        db.session.commit()
        rent_car(car_id)
        return redirect(url_for("success_forms"))

    return render_template(
        "reservation.html", form=form, current_picture=test.get("photo")
    )


def rent_car(car_id):
    customer = Customer.query.filter(Customer.car_id == car_id).one()
    rent=Rent()
    rent.car_id = car_id
    rent.customer_id = customer.id
    rent.price = session["price"]
    rent.return_date = session["rent-to"]
    rent.pickUp_date = session["rent-from"]
    db.session.add(rent)
    db.session.commit()

@app.route("/success/", methods=["POST"])
def success_forms():
    print(request.form)
    return render_template("base.html")
