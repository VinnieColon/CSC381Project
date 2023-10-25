# This is the main file of our app that will contain our flask routes
# This file will be the one that is running when we use our app


# Imports
from flask import Flask, render_template, redirect, request, url_for, flash
from FormatDataframe import fmtDataframe
import pandas as pd
from StdForms import StandardizeColsForm
from scipy.stats import zscore
from standard import scaleData
from werkzeug.utils import secure_filename
from allowed_file import allowed_file
import os


# These are env vars that need to be set for app to work
app = Flask(__name__)
app.config["SECRET_KEY"]='Smokin shit in a glass pipe'
app.config['UPLOAD_FOLDER']='uploads' # This defines the upload folder as storage folder for user uploaded files


# This is called the root route because it corresponds to "/"
# This route will display a form allowing user to input a csv file
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('main_datatable', filename=filename))
    return render_template('upload_csv.html')


# This is the route for our data table
@app.route("/main_datatable/<filename>")
def main_datatable(filename):
    df = pd.read_csv('uploads/{}'.format(filename))
    result = fmtDataframe(df)
    return render_template('dataTable.html', title="Main Datatable", header="Main Datatable", name=filename, result=result)


# This is the route for the form to standardize the data
@app.route("/standardize_data/<filename>", methods=['GET', 'POST'])
def standardize_data(filename):

    # Read in current csv from uploads
    statsDF = pd.read_csv('uploads/{}'.format(filename))
    statsDF.drop(statsDF.columns[statsDF.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

    # Define our form and populate column choices from the input data
    # Note that we will only allow columns with float values to be standardized
    form = StandardizeColsForm()
    cols = []
    for col in statsDF.select_dtypes('floating').columns:
        cols.append(tuple([col, col]))
    form.chosenCols.choices = cols

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
        return render_template('dataTable.html', title="Standardized Table", header="Standardized Table", name=filename, result=res)

    # If not yet submitted, we keep rendering standardize_data template
    return render_template('standardize_data.html', title="Standardize Data", header="Standardize Data", form=form, name=filename)


# This must be in this file for flask to work correctly
if __name__ == "__main__":
   app.run(debug=True)  