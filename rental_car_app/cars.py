from flask import jsonify, render_template, request, url_for, redirect, session
from flask_login import login_required, login_user, logout_user, current_user

from rental_car_app import app
from rental_car_app.models.Cars import Cars
from rental_car_app.models.Rent import Rent
from rental_car_app.models.Price import Price
from rental_car_app.models.Customer import Customer
from rental_car_app.Control.PriceCounter import PriceCounter
from rental_car_app.Control.DataComparator import DataComparator
from rental_car_app import db
from rental_car_app import utils
from flask_login import LoginManager

from rental_car_app.Forms.SearchDate import SearchDate
from rental_car_app.Forms.CustomerData import CustomerData


@app.route("/first", methods=["GET", "POST"])
def main_page():
    return render_template("first_page.html")


@app.route("/", methods=["GET", "POST"])
def get_cars():
    # cars = Cars.query
    rents = Rent.query
    forms2 = SearchDate()
    rent_list = []
    for rent in rents:
        rent_list.append(rent.to_json())

    if request.method == "GET":
        return render_template(
            "get_cars_template.html", form1=forms2, current_picture="cars.jpg"
        )
    elif request.method == "POST":
        cars = Cars.query
        form_list = []
        if (
            request.form.get("rent-from") != None
            and request.form.get("rent-to") != None
        ):
            session["rent-from"] = request.form.get("rent-from")
            session["rent-to"] = request.form.get("rent-to")
            data_comparator = DataComparator(
                session["rent-from"], session["rent-to"], rent_list
            )
            reserved_cars = data_comparator.check_car_avability()
            for car in cars:
                if car.to_json()["id"] in reserved_cars:
                    continue
                else:
                    form_list.append(car.to_json())
            session["form_list"] = form_list
            print(session["form_list"])

            return render_template(
                "get_cars_template.html",
                form1=forms2,
                form=form_list,
                calendar=session,
                current_picture="cars.jpg",
            )
        elif request.form.get("name") != None:
            result = request
            requests = result.values
            _index = int(requests.get("id"))
            true_index = (
                list(map(lambda x: x["id"] == _index, session["form_list"]))
            ).index(True)
            return render_template(
                "get_cars_template.html",
                form1=forms2,
                form=form_list,
                current_picture=session["form_list"][true_index]["photo"],
                datas=session["form_list"][true_index],
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
    price.exchange_value("PLN")
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
    rent = Rent()
    rent.car_id = car_id
    rent.customer_id = customer.id
    rent.price = session["price"]
    rent.return_date = session["rent-to"]
    rent.pickUp_date = session["rent-from"]
    db.session.add(rent)
    db.session.commit()


def set_currency(currency):
    session["currency"] = currency


@app.route("/success/", methods=["POST"])
def success_forms():
    print(request.form)
    return render_template("base.html")
