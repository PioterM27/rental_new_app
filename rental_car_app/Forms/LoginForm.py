from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    SubmitField,
    PasswordField,
    StringField,
    IntegerField,
    PasswordField,
)


class LoginForm(FlaskForm):
    email = StringField("Email adress")
    password = PasswordField("Password")
