from flask_wtf import Form
from wtforms import StringField, IntegerField, DateField,  PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email, Length, EqualTo)
from wtforms.fields.html5 import DateField


class JournalEntry(Form):
    title = StringField('Title')
    dateCreated = DateField('Date Created')
    timeSpent = IntegerField('Time Spent')
    learned = TextAreaField('What I learned')
    resources = TextAreaField('Helpful resources')


