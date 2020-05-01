from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):

    #attribute = value('arguments')
    username = StringField('Username', validators = [Length(min = 2, max = 30), DataRequired()])
    email = StringField('Email', validators = [Length(min = 5, max = 50), DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 4, max = 50)])
    confirm_password = PasswordField('Confirm Password', validators = [Length(min = 4, max = 50), DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):

    email = StringField('Email', validators = [Length(min = 5, max = 50), DataRequired(), Email()])
    username = StringField('Username', validators = [Length(min = 2, max = 30), DataRequired()])
    password = PasswordField('Password', validators = [Length(min = 4, max = 50), DataRequired()])
    #use cookies to stay logged in by importing the boolean field
    remember = BooleanField('Remember Me')
    #create a new SubmitField, this one with the label of "login"
    submit = SubmitField('Log In')
