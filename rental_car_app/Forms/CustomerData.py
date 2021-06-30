from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, PasswordField, StringField, IntegerField


class CustomerData(FlaskForm):
    first_name = StringField("Name")
    last_name = StringField("Last Name")
    email = StringField("Email")
    adress = StringField("123 Main St")
    age = IntegerField("Age")
    city = StringField("City")
    submit = SubmitField("Search")
