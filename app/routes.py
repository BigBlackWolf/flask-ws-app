from flask import Blueprint, render_template, flash, redirect, url_for, session
from flask_login import current_user, login_user, login_required, logout_user
from app.forms import LoginForm, RegistrationForm
from app.models import User
from app import db


main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    return render_template('chat.html')


@main.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        session['username'] = form.username.data
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form)


@main.route('/register', methods=('GET', 'POST'))
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are registered now!')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)


@main.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('main.index'))

