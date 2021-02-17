from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ipForm(FlaskForm):
    ipInput = StringField('IP address')
    submit = SubmitField('Submit')