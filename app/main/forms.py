from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField, DateTimeField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length

class SessionForm(FlaskForm):
    
    title = StringField("Title", validators = [DataRequired()])
    description = StringField("Description")
    location = StringField("Location", validators = [DataRequired()])
    datetime = StringField("Date(s)", validators = [DataRequired()])
    reoccuring = BooleanField("Reoccuring?")
    submit = SubmitField("Post Session")
    
class EventForm(FlaskForm):
    title = StringField("Title", validators = [DataRequired()])
    description = StringField("Description")
    location = StringField("Location", validators = [DataRequired()])
    datetime = StringField("Date(s)", validators = [DataRequired()])
    submit = SubmitField("Post Event")
