from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    age = StringField("Age", validators=[DataRequired()])

class BookForm(FlaskForm):
    title = StringField('Title')
    author = StringField('Author')
    genre = StringField('Genre')
    description = TextAreaField('Description')