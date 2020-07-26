from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from ...Models import User

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That Username is taken. Please try another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('An account with that email already exists.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class UpdateProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=20)])
    profile_picture = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    header = FileField('Header', validators=[FileAllowed(['jpg', 'png'])])
    bio = TextAreaField('Bio', validators=[Length(max=280)])
    submit = SubmitField('Update')