from flask_wtf import FlaskForm
from wtforms.fields.html5 import TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import StringField, PasswordField, SubmitField, BooleanField

# Putting fields where you need to enter your name, password, confirm password


class RegistrationForm(FlaskForm):
   # DataRequired() makes it so you need to put something in the field ( length chosen from 3 to 16 characters long)
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=3, max=16)])

    # Email() makes sure the email is valid
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class TimeInput(FlaskForm):
    duration = TimeField('Watering duration', format='%H:%M',
                         validators=[DataRequired()])
    submit = SubmitField('Submit')
