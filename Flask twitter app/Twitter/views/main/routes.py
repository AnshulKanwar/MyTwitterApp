from datetime import datetime

from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user

from ...Models import Tweet

main = Blueprint("main", __name__)


@main.route("/home")
@login_required
def home():
    feed = Tweet.query.order_by(Tweet.date_posted.desc()).all()
    current_time = datetime.utcnow()
    return render_template("main/feed.html", title='Home', feed=feed, current_time=current_time)