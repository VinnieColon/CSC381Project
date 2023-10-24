# This file will contain the definition for the form that will be used to select the columns to be standardized
# and the range to which they will be standardized


# Imports
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SelectField, SubmitField
import pandas as pd
from wtforms.validators import InputRequired


# Read in stats.csv, we will need it to populate our forms
statsDF = pd.read_csv('/static/data/stats.csv')
statsDF.drop(statsDF.columns[statsDF.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)


# Getting the column names and formatting them for form
cols = statsDF.columns
i = 1
colChoices = []
for col in cols:
    colChoices.append(tuple([str(i), col]))
    i += 1


# Defining ranges for standardization (will be fixed for now)
ranges = [
    ('1', '0-1'), 
    ('2', '0-10'),
    ('3', '-1-1'),
    ('4', '1-10'),
    ('5', 'z')
]


# Defining the form for standardizing selected columns to a specified range
class StandardizeColsForm(FlaskForm):

    # This is the field for selecting one or more columns
    chosenCols = SelectMultipleField('Choose Columns', validators=[InputRequired("Must choose at least one")], choices=colChoices)

    # This is the field for selecting the range
    chosenRange = SelectField('Choose Range', validators=[InputRequired("Must choose one")], choices=ranges)

    # This is the submit field
    submit = SubmitField('Submit')