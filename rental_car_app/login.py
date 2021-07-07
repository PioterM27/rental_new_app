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
from rental_car_app.models.User import User
from rental_car_app.Forms.LoginForm import LoginForm
from rental_car_app.Forms.RegistrationForm import RegistrationForm


@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegistrationForm()
    if request.method == "GET":
        return render_template("loginView.html", register_form=register_form)
    elif request.method == "POST":
        return redirect(url_for("admin_panel"))


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "GET":
        return render_template("loginView.html", login_form=login_form)
    elif request.method == "POST":
        print(request.form)
        return render_template("base.html")


@app.route("/logout", methods=["POST"])
def logout():
    crn_user = current_user.is_authenticated
    if crn_user:
        crn_user_name = current_user.username
        logout_user()
        return (
            jsonify(
                {"status": 200, "current_user": f"User {str(crn_user_name)} logout"}
            ),
            200,
        )
    else:
        return (
            jsonify({"status": 404, "message": "Any user available at this session"}),
            404,
        )
