from flask import Flask, render_template
from flask import request
from flask_mysqldb import MySQL
from flask_wtf import Form
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import smtplib
from twilio.rest import Client

from Demographic_Information import Demographic_Information
from Contact_Information import Contact_Information
from Household_and_Family_Information import Household_and_Family_Information
from Public_Assistance_Benefits import Public_Assistance_Benefits
from Prefix_Page import Prefix_Page

DEBUG = True
app = Flask(__name__)

mysql  = MySQL()

#config mySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'theNurseNeedsFiles18#'
app.config['MYSQL_DB'] = 'team6'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql.init_app(app)

#class UploadForm(Form):
#    file = FileField()

#@app.route('/page1', methods=['GET', 'POST'])
#def page1():
#    contactInformationForm = Contact_Information(request.form)
#
#    return render_template('page1.html', form=contactInformationForm)

@app.route('/')
def index():
    return render_template('SERJobsHome.html')

class ReusableForm(Form):
    name = TextAreaField('Name:', validators=[validators.data_required()])

@app.route('/page5', methods=['GET', 'POST'])
def page5():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    passw = 'SERHouston18'
    smtpObj.login('serhoustonautotext@gmail.com', passw)
    smtpObj.sendmail('cristiangonzalez1998@gmail.com', 'cristiangonzalez1998@gmail.com',
                     'Subject: Finished Application\nHello, Congratulations on completing your applications with SER Houston. We will come in contact with you in 3-5 business days. Our offices are open Tuesday at 1:30 pm for information meetings!')
    accountSID = 'AC372eea480291ec92b30cb06e264bd80c'
    authToken = '4db44f599dec7241b97e386fd0e69ffc'
    client = Client(accountSID, authToken)
    myTwilioNumber = '+19728489497'
    myCellPhone = '+14693860594'
    message = client.messages.create(
        to=myCellPhone,
        from_=myTwilioNumber,
        body="Hello, Congratulations on completing your applications with SER Houston. We will come in contact with you in 3-5 business days. Our offices are open Tuesday at 1:30 pm for information meetings!")

    return render_template('page5.html')

@app.route('/page4', methods=['GET', 'POST'])
def page4():
    form = Public_Assistance_Benefits(request.form)
    return render_template('page4.html', form=form)

@app.route('/page3', methods=['GET', 'POST'])
def page3():
    form = Demographic_Information(request.form)
    if request.method == 'POST':
        gender                  = form.gender.data
        hispanicOrLatino        = form.hispanicOrLatino.data
        race                    =  form.race.data
        #otherLanguages          = form.otherLanguages.data
        #specialAccommodations   = form.specialAccommodations.data
        workAuthorization        = form.workAuthorization.data
        citizenship              = form.citizenship.data
        validID                  = form.validID.data
        primaryTransportation    = form.primaryTransportation.data
        housingStatus            = form.housingStatus.data
        ageOver24                = form.ageOver24.data

        cur1 = mysql.connection.cursor()

        print("About to Execute!")

        insertString = "INSERT INTO demographic_info(gender, hispanicOrLatino, race, workAuthorization, citizenship, validID, primaryTransportation, housingStatus, ageOver24) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (gender, hispanicOrLatino, race, workAuthorization, citizenship, validID, primaryTransportation, housingStatus, ageOver24)
        print(insertString)
        cur1.execute("INSERT INTO demographic_info(gender, hispanicOrLatino, race, workAuthorization, citizenship, validID, primaryTransportation, housingStatus, ageOver24) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (gender, hispanicOrLatino, race, workAuthorization, citizenship, validID, primaryTransportation, housingStatus, ageOver24))

        print("Executed!")
        mysql.connection.commit()

        cur1.close()

    form = Household_and_Family_Information(request.form)
    return render_template('page3.html', form=form)


@app.route('/page1', methods=['GET', 'POST'])
def page1():
    form = Contact_Information(request.form)
    return render_template('page1.html', form=form)

@app.route('/page2', methods=['GET', 'POST'])
def page2():
    form = Contact_Information(request.form)
    print("Hello2")
    if request.method == 'POST':
        print("I want to assign vars")
        firstName           = form.firstName.data
        middleName          = form.middleName.data
        lastName            = form.lastName.data
        referral            = form.referral.data
        streetAddress       = form.streetAddress.data
        city                = form.city.data
        state               = form.state.data
        postalCode          = form.postalCode.data
        county              = form.county.data
        socialSecurity      = form.socialSecurity.data
        dateOfBirth         = form.dateOfBirth.data
        email               = form.email.data
        workPhone           = form.workPhone.data
        mobilePhone         = form.mobilePhone.data
        homePhone           = form.homePhone.data
        preferredPhone      = form.preferredPhone.data
        facebookPage        = form.facebookPage.data
        twitterHandle       = form.twitterHandle.data
        instagramUsername   = form.instagramUsername.data
        #linkedIn            = form.linkedIn.data

        cur = mysql.connection.cursor()

        print("About to Execute!")
        cur.execute("INSERT INTO contact_Informaton(firstName, middleName, lastName, referral, streetAddress, city, state, postalCode, county, socialSecurity, dateOfBirth, email, workPhone, mobilePhone, homePhone, preferredPhone, facebookPage, twitterHandle, instagramUsername) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (firstName, middleName, lastName, referral, streetAddress, city, state, postalCode, county, socialSecurity, dateOfBirth, email, workPhone, mobilePhone, homePhone, preferredPhone, facebookPage, twitterHandle, instagramUsername))

        print("Executed!")
        mysql.connection.commit()

        cur.close()

    form = Demographic_Information(request.form)
    return render_template('page2.html', form=form)


@app.route('/apply')
def apply():
    return render_template('apply.html')

if __name__ == '__main__':
    app.run(
    host='127.0.0.1',port=8080,debug=True)
