from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Regexp, DataRequired, Length

class WTForms(FlaskForm):
    product_id = StringField("", #etykieta

    validators=[
        Regexp("^[0-9]+$", message="Kod zawiera litery"), #$ to avoid partial match
        DataRequired(message="Obszar jest pusty"),
        Length(min=6, max=10, message="Niepoprawna długość kodu")
        
        ]
        )
    submit = SubmitField("Submit")
 
 