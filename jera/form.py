from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, validators

class RegistrationForms(FlaskForm):
    idnum = StringField('ID number', [validators.data_required(message=('You must fill in this part')), validators.Length(min=9, message=('Invalid'), max=9)])
    firstname = StringField('First Name', [validators.data_required(message=('You must fill in this part')), validators.Length(min=3, message=('Too short. Must be 3 characters and above.'), max=20)])
    middlename = StringField('Middle Name', [validators.data_required(message=('You must fill in this part')), validators.Length(min=2, message=('Too short. Must be 2 characters and above.'), max=20)])
    lastname = StringField('Last Name', [validators.data_required(message=('You must fill in this part')), validators.Length(min=2, message=('Too short. Must be 2 characters and above.'), max=20)])
    sex = RadioField('Sex', choices=[('M', 'Male'), ('F', 'Female')])
    course = StringField('Course', [validators.data_required(message=('You must fill in this part')), validators.Length(min=4, message=('Too short. Must be 4 characters and above'), max=5)])
    submit = SubmitField('Submit')