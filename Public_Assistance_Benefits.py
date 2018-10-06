from wtforms import Form, BooleanField, StringField, validators, SelectField, IntegerField,SelectMultipleField


class Public_Assistance_Benefits(Form):
    receivingPublicAssistance = SelectMultipleField('Are you currently receiving any of the following forms of public assistance?', choices=[('1','Breakfast & Lunch Program'),('2', "CHIP (Children's Medicaid"),('3', 'CEAP (Comprehensive Energy Asst Program'),('4', 'Headstart'),('5', 'Medicaid'),('6', 'SFSP (Summer Food Service Program)'),('7', 'SMP (Special Milk Program)'),('8', 'SNAP (Supplemental Nutrition Asst Program)'),('9', 'TANF (TexasTemp. Asst for Needy Families)'),('10', 'WAP (Weatherization Asst Program)'),('11', 'WIC (Women, Infants, and Children)')])
    registeredSelectiveService = SelectField('Are you registered with a selective service?', choices=[('1','Please select...'), ('2', 'Yes'), ('3', 'No'), ('4', 'Not Sure'), ('5', 'Not Applicable')])