from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import login_user, current_user, logout_user, login_required

from Twitter import bcrypt, db
from .forms import RegisterForm, LoginForm, UpdateProfileForm
from ...Models import User, Tweet
from .utils import save_picture, save_header


user = Blueprint('user', __name__)


@user.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now Log in', 'success')
        return redirect(url_for('user.login'))
    return render_template('user/register.html', form=form)


@user.route('/', methods=['GET', 'POST'])
@user.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        flash('Your username or password is incorrect. Please try again', 'danger')
    return render_template('user/login.html', form=form)


@user.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have succesfully logged out', 'success')
    return redirect(url_for('user.login'))


@user.route('/<string:username>')
@login_required
def display_profile(username):
    user = User.query.filter_by(username=username).first()
    tweets = Tweet.query.filter_by(author=user).order_by(Tweet.date_posted.desc()).all()
    return render_template('user/profile.html', user=user, tweets=tweets, n_tweets = len(tweets))


@user.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if form.profile_picture.data:
            picture = save_picture(form.profile_picture.data)
            current_user.profile_picture = picture
        else:
            current_user.profile_picture = 'default.png'
        if form.header.data:
            picture = save_header(form.header.data)
            current_user.header = picture
        else:
            current_user.header = None
        current_user.name = form.name.data
        current_user.bio = form.bio.data
        db.session.commit()
        return redirect(url_for('user.display_profile', username=current_user.username))

    elif request.method == 'GET':
        form.name.data = current_user.name
        form.bio.data = current_user.bio
    return render_template('user/edit_profile.html', title='Profile', form=form)
