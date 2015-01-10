__author__ = 'heinrich'
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, FloatField, DateField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email


class RegisterForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordConfirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', 'Passwords did not match')])
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname')


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class IncomeForm(Form):
    amount = FloatField('Amount', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    incomeType = SelectField('Income Type', validators=[DataRequired()])
    newIncomeType = StringField('Income Type')