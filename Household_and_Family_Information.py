from wtforms import Form, BooleanField, StringField, validators, SelectField, IntegerField


class Household_and_Family_Information(Form):
    maritalStatus = SelectField('Marital Status *', choices=[('1','Please select...'), ('2','Single'), ('3','Married'),('4','Divorced'),('5','Separated'), ('6','Widow/Widower')])
    householdAnnualIncome = SelectField("What is your household's annual income? *", choices=[('1','Please select...'), ('2', 'Below $5,000'), ('3', '$5,000 - 10,000'),('4', '$10,001 - 15,000'),('5', '$15,001 - 20,000'),('6', '$20,001 - 25,000'),('7', '$25,001 - 30,000'), ('8', '$30,001 - 35,000'),('9', '$35,001 - 40,000'), ('10', '$40,001 - 45,000'),('11', '$45,001 - 50,000')])
    childrenUnder18 = IntegerField('How many children 17 years old and under live in your household? *', [validators.Length(min=0, max=120)])
    adults18To24 = IntegerField('How many young adults 18-24 years old live in your household? *', [validators.Length(min=0, max=120)])
    adults = IntegerField('How many adults live in your household?', [validators.Length(min=0, max=120)])
    checkingAccount = SelectField('Do you have a checking account? *', choices=[('1', 'Please select...'), ('2', 'Yes'), ('3', 'No')])
    savingsAccount = SelectField('Do you have a savings account? *',choices=[('1', 'Please select...'), ('2', 'Yes'), ('3', 'No')])
    paydayLoan = SelectField('Do you have a payday loan? *',choices=[('1', 'Please select...'), ('2', 'Yes'), ('3', 'No')])
    carTitleLoan = SelectField('Do you have a car title loan? *',choices=[('1', 'Please select...'), ('2', 'Yes'), ('3', 'No')])
