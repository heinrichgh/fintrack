__author__ = 'heinrich'
from flask import render_template, flash, g, redirect, url_for
from app import app, db, lm
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import RegisterForm, LoginForm, IncomeForm
from .models import User


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
        None
    return render_template('specify_income.html', title='Specify Income', form=form)


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