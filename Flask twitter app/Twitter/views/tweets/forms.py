from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class NewTweet(FlaskForm):
    content = TextAreaField(validators=[DataRequired(), Length(min=1, max=280)])
    tweet = SubmitField('Tweet')