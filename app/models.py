__author__ = 'heinrich'
from app import db


class User(db.Model):
    ipkUserID = db.Column(db.Integer, primary_key=True)
    sEmail = db.Column(db.String(128), index=True, unique=True)
    sPassword = db.Column(db.String(128), index=True)
    sName = db.Column(db.String(32))
    sSurname = db.Column(db.String(32))
    incomes = db.relationship('Income', backref='user', lazy='dynamic')
    incomeTypes = db.relationship('IncomeType', backref='user', lazy='dynamic')
    expenditures = db.relationship('Expenditure', backref='user', lazy='dynamic')
    expenditureTypes = db.relationship('ExpenditureType', backref='user', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def __repr__(self):
        return '<User %r>' % self.sEmail


class Income(db.Model):
    ipkIncome = db.Column(db.Integer, primary_key=True)
    ifkUserID = db.Column(db.Integer, db.ForeignKey('user.ipkUserID'))
    ifkIncomeType = db.Column(db.Integer, db.ForeignKey('income_type.ipkIncomeType'))
    fAmount = db.Column(db.Float)
    incomeType = db.relationship('IncomeType', backref='income', lazy='dynamic')


class IncomeType(db.Model):
    ipkIncomeType = db.Column(db.Integer, primary_key=True)
    ifkUserID = db.Column(db.Integer, db.ForeignKey('user.ipkUserID'))
    sType = db.Column(db.String(32))


class Expenditure(db.Model):
    ipkExpenditure = db.Column(db.Integer, primary_key=True)
    ifkUserID = db.Column(db.Integer, db.ForeignKey('user.ipkUserID'))
    ifkExpenditureType = db.Column(db.Integer, db.ForeignKey('expenditure_type.ipkExpenditureType'))
    fAmount = db.Column(db.Float)
    expenditureType = db.relationship('ExpenditureType', backref='expenditure', lazy='dynamic')


class ExpenditureType(db.Model):
    ipkExpenditureType = db.Column(db.Integer, primary_key=True)
    ifkUserID = db.Column(db.Integer, db.ForeignKey('user.ipkUserID'))
    sType = db.Column(db.String(32))