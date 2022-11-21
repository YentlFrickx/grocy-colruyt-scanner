from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField, PasswordField, StringField

class ConnectForm(FlaskForm):
    grocy_api_key = StringField('Api key')
    colruyt_email = EmailField('Colruyt email')
    colruyt_password = PasswordField('Colruyt password')
    submit = SubmitField('Submit')
