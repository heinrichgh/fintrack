__author__ = 'heinrich'
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(Form):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordConfirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', 'Passwords did not match')])
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname')