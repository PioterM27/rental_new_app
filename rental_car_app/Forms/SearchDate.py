from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField


class SearchDate(FlaskForm):
    dateFrom = DateField("Rent from dd-mm-yyyy")
    dateTo = DateField("Rent to dd-mm-yyyy")
    submit = SubmitField("Search")
