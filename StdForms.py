# This file will contain the definition for the form that will be used to select the columns to be standardized
# and the range to which they will be standardized


# Imports
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SelectField, SubmitField, widgets
import pandas as pd


# Read in stats.csv, we will need it to populate our forms
statsDF = pd.read_csv('static/data/stats.csv')
statsDF.drop(statsDF.columns[statsDF.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)


# Getting the column names and formatting them for form
cols = statsDF.columns
colChoices = []
for col in cols:
    colChoices.append(tuple([col, col]))


# Creating list of tuples that will be passed to the form
rangeChoices = [('0-1', '0-1'), ('0-10', '0-10'), ('-1-1', '-1-1'), ('1-10', '1-10'), ('z', 'z')]


# Defining a MultiCheckboxField as an extension of the SelectMultipleField
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


# Defining the form for standardizing selected columns to a specified range
class StandardizeColsForm(FlaskForm):

    # This is the field for selecting one or more columns
    chosenCols = MultiCheckboxField('Choose Columns', choices=colChoices)

    # This is the field for selecting the range
    chosenRange = SelectField('Choose Range', choices=rangeChoices)

    # This is the submit field
    submit = SubmitField('Submit')