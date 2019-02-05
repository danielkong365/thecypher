from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField, DateTimeField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length
from wtforms.fields.html5 import DateField

class SessionForm(FlaskForm):
    
    title = StringField("Title", validators = [DataRequired()])
    description = StringField("Description")
    location = StringField("Location", validators = [DataRequired()])
    date = DateField("Date(s)")
    reoccuring = BooleanField("Reoccuring?")
    submit = SubmitField("Post Session")
    
class EventForm(FlaskForm):
    title = StringField("Title", validators = [DataRequired()])
    description = StringField("Description")
    location = StringField("Location", validators = [DataRequired()])
    date = DateField("Date(s)")
    submit = SubmitField("Post Event")
