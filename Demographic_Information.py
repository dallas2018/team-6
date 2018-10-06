from wtforms import Form, SelectField, SelectMultipleField


class Demographic_Information(Form):
    gender                  = SelectField('Gender *', choices=[('1','Please select...'), ('2','Female'), ('3','Male'),('4','Transgender')])
    hispanicOrLatino        = SelectField('Do you consider yourself Hispanic or Latino? *', choices=[('1','Please select...'), ('2','Yes'), ('3','No')])
    race                    = SelectField('Race *', choices=[('1','Please select...'), ('2', 'Black or African American'),('3', 'American Indian or Alaskan Native'), ('4','Asian (not Pacific Islander)'),('5','Hawaiian Native or Pacific Islander'),('6', 'White or Caucasion'), ('7','Two or More'),('8', 'Other')])
    otherLanguages          = SelectMultipleField('Do you speak any languages other than English? * Check all that apply. Please check the "Not Applicable" box if you do not speak another language.', choices=[('1','African Languages'), ('2','Chinese'),('3', 'German'), ('4','Japanese'),('5' ,'Persian'),('6', 'Russian'),('7', 'Vietnamese'),('8','Arabic'),('9', 'French'),('10','Italian'),('11', 'Korean'),('12', 'Portuguese'), ('13','Spanish or Spanish Creole'),('14','Other'), ('15','Not Applicable')])
    specialAccommodations   = SelectMultipleField('Do you need any special accommodations in order to participate in training or performing tasks at work? * \nCheck all that apply. Please check the "Not Applicable" box if you do need any special accommodations.', choices=[('1','Visual'),('2','Speech'),('3', 'Hearing'),('4', 'Limited Mobility'),('5', 'Not Applicable')])
    workAuthorization       = SelectField('Are you authorized to work in the United States? *',choices=[('1','Please select...'), ('2','Yes'), ('3','No')])
    citizenship             = SelectField('I attest, under penalty of perjury, that I am a (choose one of the following): *', choices=[('1','Please select...'), ('2','Citizen of the United States'),('3', 'Non-citizen National of the United States'),('4','Lawful Permanent Resident')])
    validID                 = SelectField('Do you have a valid form of identification? *',choices=[('1','Please select...'), ('2','Yes'), ('3','No')])
    primaryTransportation   = SelectField('What is your primary method of transportation? *', choices=[('1','Please select...'), ('2','Own/lease vehicle'), ('3','Can borrow vehicle'), ('4','Public Transit'), ('5','Own/lease vehicle but it is not operable/reliable')])
    housingStatus           = SelectField('What is your housing status? *', choices=[('1','Please select...'), ('2','Homeowner'), ('3','Renter-Unsubsidized (not receiving public assistance)'), ('4','Renter-Subsidized (receiving public assistance to cover your rent)'), ('5','Living with a friend/family'), ('6','Staying in a shelter'), ('7','Homeless')])
    ageOver24               = SelectField('Are you over 24? *', choices=[('1','Please select...'), ('2','Yes'), ('3','No')])
