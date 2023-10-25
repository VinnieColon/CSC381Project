# This is the main file of our app that will contain our flask routes
# This file will be the one that is running when we use our app


# Imports
from flask import Flask, render_template, url_for, request, redirect
from FormatDataframe import fmtDataframe
import pandas as pd
from StdForms import StandardizeColsForm
from scipy.stats import zscore
from standard import scaleData


# These are env vars that need to be set for app to work
app = Flask(__name__)
app.config["SECRET_KEY"]='Smokin shit in a glass pipe'


# This is called the root route because it corresponds to "/"
# For now this will just redirect to the route for our datatable page
@app.route("/")
def main_redirect():
    return redirect(url_for('main_datatable'))


# This is the route for our data table
@app.route("/main_datatable")
def main_datatable():
    df = pd.read_csv('static/data/stats.csv')
    result = fmtDataframe(df)
    return render_template('dataTable.html', title="Main Datatable", header="Main Datatable", result=result)


# This is the route for the form to standardize the data
@app.route("/standardize_data", methods=['GET', 'POST'])
def standardize_data():

    # Define our form
    form = StandardizeColsForm()

    # Read in stats.csv
    statsDF = pd.read_csv('static/data/stats.csv')
    statsDF.drop(statsDF.columns[statsDF.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

    # Check if valid submission made to form
    if form.validate_on_submit():

        # Get attribute of the flask request object corresponding to our form
        # This contains the entries made and submitted by the user
        colsChosen = form.chosenCols.data
        rangeChosen = form.chosenRange.data

        # Standardizing chosen columns to chosen range
        if rangeChosen == 'z':
            for col in colsChosen:
                curr = zscore(statsDF[col])
                statsDF.drop(statsDF.columns[statsDF.columns.str.contains(col, case = False)],axis = 1, inplace = True)
                statsDF[col] = curr
        else:
            # Getting low and high bound of range as integers
            low, high = 0, 0
            if rangeChosen[0] == '-':
                low, high = -1, 1
            else:
                splitRange = rangeChosen.split('-')
                low = int(splitRange[0])
                high = int(splitRange[1])
            
            for col in colsChosen:
                curr = scaleData(statsDF[col].to_numpy(), low, high)
                statsDF.drop(statsDF.columns[statsDF.columns.str.contains(col, case = False)],axis = 1, inplace = True)
                statsDF[col] = curr
        
        # Now we can format and render this augmented table
        res = fmtDataframe(statsDF)
        return render_template('dataTable.html', title="Standardized Table", header="Standardized Table", result=res)

    # If not yet submitted, we keep rendering standardize_data template
    size = len(statsDF.columns)
    return render_template('standardize_data.html', title="Standardize Data", header="Standardize Data", form=form, size=size)


# This must be in this file for flask to work correctly
if __name__ == "__main__":
   app.run(debug=True)  