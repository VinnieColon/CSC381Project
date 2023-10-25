# This script takes the rows of the csv data and transforms them into the format needed to work with flask and templates
# Format: Data passed as a list of dictionaries where each dictionary represents a row, keys are column names and values are entries
# This will be important for when we create our routes that will link our template to a url

# Imports
import pandas as pd


# Defining a function that will format a pandas dataframe for rendering
def fmtDataframe(df: pd.DataFrame):

    # Drops any unnamed columns
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

    # For each row we create a dictionary where key is column name and value is entry at that column and row
    res = []
    for i in range(len(df.index)):
        curr = {}
        for col in df.columns:
            curr[col] = df.iloc[i][col]
        res.append(curr)

    # Return resulting list of dictionaries
    return res


# Below is an example of it being used on stats.csv
statsDF = pd.read_csv('static/data/stats.csv')
fmtData = fmtDataframe(statsDF)

# Printing keys and values of dictionary representing the first row
#for k, v in fmtData[0].items():
    #print("Key: {} \nValue: {}\n".format(k, v))