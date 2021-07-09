from rental_car_app import login_manager
from rental_car_app.models.User import User
from rental_car_app import db

@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return User.query.get(str(user_id))