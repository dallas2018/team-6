from flask import Flask, render_template
from flask import request
# from flask_wtf import Form
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

from Demographic_Information import Demographic_Information
from Contact_Information import Contact_Information

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

#class UploadForm(Form):
#    file = FileField()

#@app.route('/page1', methods=['GET', 'POST'])
#def page1():
#    contactInformationForm = Contact_Information(request.form)
#
#    return render_template('page1.html', form=contactInformationForm)

@app.route('/')
def index():
    return render_template('home.html')

class ReusableForm(Form):
    name = TextAreaField('Name:', validators=[validators.data_required()])

@app.route('/page2', methods=['GET', 'POST'])
def page2():

    form = Demographic_Information(request.form)
    return render_template('page2.html', form=form)
    # return render_template('page2.html', form=form)

@app.route('/page1', methods=['GET', 'POST'])
def page1():
    form = Contact_Information(request.form)
    return render_template('page1.html', form=form)

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/Modal1')
def Modal1():
    return render_template('Modal1.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)
