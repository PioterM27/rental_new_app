from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)


db = SQLAlchemy(app)
migrate = Migrate(app, db)

# results = db.session.execute('show databases')
# for row in results:
#     print(row)


from rental_car_app import cars
from rental_car_app import login
from rental_car_app import admin
from rental_car_app.models import Cars
from rental_car_app.models import Customer
from rental_car_app.models import Rent
from rental_car_app.models import User
from rental_car_app.models import Price
from rental_car_app.models import Season
from rental_car_app.models import db_manage_command
