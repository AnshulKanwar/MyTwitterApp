from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

from Twitter import db
from .forms import NewTweet
from ...Models import Tweet

tweets = Blueprint('tweets', __name__)

@tweets.route('/new_tweet', methods=['GET', 'POST'])
def new_tweet():
    form = NewTweet()
    if form.validate_on_submit():
        tweet = Tweet(content=form.content.data, author=current_user)
        db.session.add(tweet)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('tweets/new_tweet.html', title='New Tweet', form=form)