# This is the main file of our app that will contain our flask routes
# This file will be the one that is running when we use our app


# Imports
from flask import Flask, render_template, url_for, request, redirect
from FormatDataframe import fmtDataframe
import pandas as pd


# These are env vars that need to be set for app to work
app = Flask(__name__)
app.config["SECRET_KEY"]='Smokin shit in a glass pipe'


# This is called the root route because it corresponds to "/"
# For now this will just redirect to the route for our datatable page
@app.route("/")
def main_redirect():
    return redirect(url_for('dataTable'))


# This is the route for our data table
@app.route("/dataTable")
def main_datatable():
    df = pd.read_csv('static/data/stats.csv')
    result = fmtDataframe(df)
    return render_template('dataTable.html', title="Main Datatable", header="Main Datatable", result=result)


# This must be in this file for flask to work correctly
if __name__ == "__main__":
   app.run(debug=True)  