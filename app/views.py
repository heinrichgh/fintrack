__author__ = 'heinrich'
from flask import render_template, flash, g, redirect, url_for
from app import app, db, lm
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import RegisterForm, LoginForm, IncomeForm, IncomeTypeForm, ExpenditureForm, ExpenditureTypeForm
from .models import User, IncomeType, Income, Expenditure, ExpenditureType


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(sEmail=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            g.user = user
            login_user(g.user)
            return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if g.user.is_authenticated():
        redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        g.user = User(form.email.data, form.password.data, form.name.data, form.surname.data)
        db.session.add(g.user)
        db.session.commit()
        login_user(g.user)
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/specify-income', methods=['GET', 'POST'])
@login_required
def specify_income():
    form = IncomeForm()
    form.incomeType.choices = [(it.ipkIncomeType, it.sType) for it in g.user.incomeTypes.all()]
    if form.validate_on_submit():
        i = Income(ifkUserID=g.user.ipkUserID, ifkIncomeType=form.incomeType.data, fAmount=form.amount.data, dDate=form.date.data)
        db.session.add(i)
        db.session.commit()
        return redirect(url_for('specify_income'))
    return render_template('specify_income.html', title='Specify Income', form=form, incomes=g.user.incomes.all())


@app.route('/income-types', methods=['GET', 'POST'])
@login_required
def income_types():
    form = IncomeTypeForm()
    if form.validate_on_submit():
        if g.user.incomeTypes.filter_by(sType=form.type.data).first() is not None:
            form.type.errors.append('Type already exists')
        else:
            it = IncomeType(ifkUserID=g.user.ipkUserID, sType=form.type.data)
            db.session.add(it)
            db.session.commit()
            return redirect(url_for('income_types'))
    return render_template('income_types.html', title='Specify Income', form=form, types=g.user.incomeTypes.all())


@app.route('/specify-expense', methods=['GET', 'POST'])
@login_required
def specify_expenditure():
    form = ExpenditureForm()
    form.expenditureType.choices = [(et.ipkExpenditureType, et.sType) for et in g.user.expenditureTypes.all()]
    if form.validate_on_submit():
        e = Expenditure(ifkUserID=g.user.ipkUserID, ifkExpenditureType=form.expenditureType.data, fAmount=form.amount.data, dDate=form.date.data)
        db.session.add(e)
        db.session.commit()
        return redirect(url_for('specify_expenditure'))
    return render_template('specify_expenditure.html', title='Specify Expense', form=form, expenditures=g.user.expenditures.all())


@app.route('/expense-types', methods=['GET', 'POST'])
@login_required
def expenditure_types():
    form = ExpenditureTypeForm()
    if form.validate_on_submit():
        if g.user.expenditureTypes.filter_by(sType=form.type.data).first() is not None:
            form.type.errors.append('Type already exists')
        else:
            et = ExpenditureType(ifkUserID=g.user.ipkUserID, sType=form.type.data)
            db.session.add(et)
            db.session.commit()
            return redirect(url_for('expenditure_types'))
    return render_template('expenditure_types.html', title='Specify Expense', form=form, types=g.user.expenditureTypes.all())


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.before_request
def before_request():
    g.user = current_user


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))