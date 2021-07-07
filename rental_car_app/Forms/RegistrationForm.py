from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, PasswordField, StringField, IntegerField


class RegistrationForm(FlaskForm):
    first_name = StringField("Name")
    last_name = StringField("Last Name")
    email = StringField("Email")
    password = PasswordField("Password")
