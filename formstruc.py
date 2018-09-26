from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, RadioField, SubmitField, SelectField
from wtforms import validators, ValidationError


class formStruct(Form):
    name = TextField("Name of student", [validators.Required("Please Enter your name.")])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    address = TextAreaField('Address')
    email = TextField('Email', [validators.Required("Please enter email."), validators.Email("Please enter valid email.")])
    age = IntegerField('Age')
    language = SelectField('Languages', choices=[('cpp', 'C++'), ('java', 'Java'), ('python', 'Python')])
    submit = SubmitField('Send')
