from wtforms import Form, BooleanField, StringField, validators, SelectField, IntegerField,SelectMultipleField

class Prefix_Page(Form):

    enterID = StringField('If you have started an application but have not completed it, enter your application ID and click Resume', [validators.Length(min=0, max=120)])
    paperApp = SelectField('If you would like a paper application, select your prefered language and click Paper', choices=[('1', 'Please select...'),('2', 'English'), ('3','Spanish'), ('4','Vietnamese')])