from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired,Email,Length

class RegistrationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(message='we need your name, it cannot be empty'), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(message='we need your email, it cannot be empty'), Email(message='that does not look like a valid email')])
    password = PasswordField('Password', validators=[DataRequired(message='we need your password, it cannot be empty'), Length(min=6)])
    submit = SubmitField('Register')
    # message = for custom error message showing