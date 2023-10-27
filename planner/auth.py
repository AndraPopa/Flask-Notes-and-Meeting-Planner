from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
            else:
                flash('Incorrect password. Try again.', category='error')
        else:
            flash('There is no account created with this email.', category='error')

    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        date_birth = request.form.get('date_birth')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        date_birth_obj = datetime.datetime.strptime(date_birth, '%Y-%m-%d')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 3 or len(last_name) < 3:
            flash('First and last name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match!', category='error')
        elif len(password1) < 7:
            flash('Password too short!', category='error')
        elif datetime.datetime.now() < date_birth_obj:
            flash('Date of birth must be in the past!', category='error')
        else:
            new_user = User(email=email,
                            password=generate_password_hash(password1),
                            first_name=first_name,
                            last_name=last_name,
                            date_birth=date_birth_obj)
            db.session.add(new_user)
            db.session.commit()
            flash('User account created successfully!', category='success')
            return redirect(url_for('views.index'))

    return render_template('signup.html')
