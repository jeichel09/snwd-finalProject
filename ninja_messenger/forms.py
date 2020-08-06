from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from ninja_messenger import db
from ninja_messenger.models import User


class RegisterForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Sign Up')

    def validate_name(self, name):
        #user = User.query.filter_by(name=name.data).first()
        user = db.session.query(User).filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('That name is taken. Please choose a different one!')

    def validate_email(self, email):
    #    user = User.query.filter_by(email=email.data).first()
        user = db.session.query(User).filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one!')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class MessageForm(FlaskForm):
    recipient = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    message = TextAreaField('Type your message here',
                                 validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Send')


