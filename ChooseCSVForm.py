# This file contains the code defining the form we will use to have a user enter file into app


# Imports
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


# Class defining the form
class FileInForm(FlaskForm):
    inFile = FileField('Choose CSV File',validators=[FileRequired(), FileAllowed('csv', 'csv files only')])