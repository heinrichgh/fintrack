__author__ = 'heinrich'
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, FloatField, DateField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email
import datetime


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
    date = DateField('Date', validators=[DataRequired()], default=datetime.date.today())
    incomeType = SelectField('Income Type', validators=[DataRequired()], coerce=int)


class IncomeTypeForm(Form):
    type = StringField('Income Type', validators=[DataRequired()])


class ExpenditureForm(Form):
    amount = FloatField('Amount', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()], default=datetime.date.today())
    expenditureType = SelectField('Expenditure Type', validators=[DataRequired()], coerce=int)


class ExpenditureTypeForm(Form):
    type = StringField('Expenditure Type', validators=[DataRequired()])