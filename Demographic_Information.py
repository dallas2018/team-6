from wtforms import Form, SelectField, SelectMultipleField


class Demographic_Information(Form):
    gender                  = SelectField('Gender *', choices=['Please select...', 'Female', 'Male', 'Transgender'])
    hispanicOrLatino        = SelectField('Do you consider yourself Hispanic or Latino? *', choices=['Please select...', 'Yes', 'No'])
    race                    = SelectField('Race *', choices=['Please select...', 'Black or African American', 'American Indian or Alaskan Native', 'Asian (not Pacific Islander)', 'Hawaiian Native or Pacific Islander', 'White or Caucasion', 'Two or More', 'Other'])
    otherLanguages          = SelectMultipleField('Do you speak any languages other than English? *\nCheck all that apply. Please check the "Not Applicable" box if you do not speak another language.', choices=['African Languages', 'Chinese', 'German', 'Japanese', 'Persian', 'Russian', 'Vietnamese', 'Arabic', 'French', 'Italian', 'Korean', 'Portuguese', 'Spanish or Spanish Creole', 'Other', 'Not Applicable'])
    specialAccommodations   = SelectMultipleField('Do you need any special accommodations in order to participate in training or performing tasks at work? * \nCheck all that apply. Please check the "Not Applicable" box if you do need any special accommodations.', choices=['Visual', 'Speech', 'Hearing', 'Limited Mobility', 'Not Applicable'])
    workAuthorization       = SelectField('Are you authorized to work in the United States? *',choices=['Please select...', 'Yes', 'No'])
    citizenship             = SelectField('I attest, under penalty of perjury, that I am a (choose one of the following): *', choices=['Please select...', 'Citizen of the United States', 'Non-citizen National of the United States', 'Lawful Permanent Resident'])
    validID                 = SelectField('Do you have a valid form of identification? *',choices=['Please select...', 'Yes', 'No'])
    primaryTransportation   = SelectField('What is your primary method of transportation? *', choices=['Please select...', 'Own/lease vehicle', 'Can borrow vehicle', 'Public Transit', 'Own/lease vehicle but it is not operable/reliable'])
    housingStatus           = SelectField('What is your housing status? *', choices=['Please select...', 'Homeowner', 'Renter-Unsubsidized (not receiving public assistance)', 'Renter-Subsidized (receiving public assistance to cover your rent)', 'Living with a friend/family', 'Staying in a shelter', 'Homeless'])
    ageOver24               = SelectField('Are you over 24? *', choices=['Please select...', 'Yes', 'No'])

