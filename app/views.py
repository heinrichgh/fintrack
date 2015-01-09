__author__ = 'heinrich'
from flask import render_template, flash
from app import app, db
from .forms import RegisterForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('Valid form')
    return render_template('register.html', title='Register', form=form)