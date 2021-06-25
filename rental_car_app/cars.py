from flask import jsonify, render_template, request, url_for
import json
from flask_wtf import FlaskForm

from rental_car_app import app
from rental_car_app.models.Cars import Cars
from rental_car_app.Forms.SearchDate import SearchDate


@app.route('/first', methods=['GET', 'POST'])
def main_page():
    return render_template("first_page.html")


@app.route('/', methods=['GET', 'POST'])
def get_cars():
    cars = Cars.query
    forms2 = SearchDate()
    formList = []
    for car in cars:
        formList.append(car.to_json())

    if request.method == 'GET':
        return render_template("get_cars_template.html", form1=forms2,
                               current_picture='cars.jpg')
    elif request.method == 'POST':
        if request.form.get('dateFrom') != None and request.form.get('dateTo') != None:
            print(request.form.get('dateFrom'))
            print(request.form.get('dateTo'))
            return render_template("get_cars_template.html", form1=forms2, form=formList,
                                   current_picture='cars.jpg')
        elif request.form.get('name') != None:
            result = request
            requests = result.values
            print(result)
            index = int(requests.get('id')) - 1
            return render_template("get_cars_template.html", form1=forms2, form=formList,
                                   current_picture=formList[index]['photo'], datas=formList[index])



@app.route("/reservation/<int:car_id>", methods=['POST'])
def get_reservation(car_id):
    print(car_id)
    test = request.values
    print(test.get('id'))
    return render_template("reservation.html", current_picture=test.get('photo'))

# @app.route('/',methods=['POST'])
# def get_car():
#     if request.method =='POST':
#         result = request.form
#         print(result)
#         return render_template("get_cars_template.html", current_picture='brava.jpg')
# @app.route('/',methods=['POST'])
# def test():
#     print("test")
#     return render_template("get_cars_template.html",form=form,current_picture='cars.jpg')
# @app.route('/')
# def index():
#     form = CarForm(csrf_enabled=False)
#     return render_template("get_cars_template.html")
# validate_on_submit waliduje wbudowane
