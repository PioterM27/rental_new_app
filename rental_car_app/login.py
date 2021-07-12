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
from flask_login import (
    login_required,
    login_user,
    logout_user,
    current_user,
    login_manager,
)

from rental_car_app import db, app
from rental_car_app.models.User import User
from rental_car_app.Forms.LoginForm import LoginForm
from rental_car_app.Forms.RegistrationForm import RegistrationForm


@app.route("/register", methods=["GET", "POST"])
def register():
    user = User()
    register_form = RegistrationForm()
    if request.method == "GET":
        return render_template("loginView.html", register_form=register_form)
    elif request.method == "POST":
        print("jest tu czy nie")
        if User.query.filter(User.email == request.form.get("email")).first():
            abort(
                409,
                description=f'User with username {request.form.get("email")} already exists',
            )

        user.password = User.generate_hashed_password(request.form.get("password"))
        user.first_name = request.form.get("first_name")
        user.last_name = request.form.get("last_name")
        user.email = request.form.get("email")
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    user = User.query.filter(User.email == request.form.get("email")).first()
    if request.method == "GET":
        return render_template("loginView.html", login_form=login_form)
    elif request.method == "POST":
        if not user.is_password_valid(request.form.get("password")):
            abort(401, description="Invalid credential")
        if user != "Guest":
            print("tutu")
            login_user(user)
            return redirect(url_for("admin_panel"))


@app.route("/logout", methods=["GET"])
def logout():
    crn_user = current_user.is_authenticated
    print(crn_user)
    if crn_user:
        crn_user_name = current_user.email
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
