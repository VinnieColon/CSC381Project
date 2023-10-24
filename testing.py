# This script takes the rows of the csv data and transforms them into the format needed to work with flask and templates
# Format: Data passed as a list of dictionaries where each dictionary represents a row, keys are column names and values are entries

import pandas as pd

statsDF = pd.read_csv('stats.csv')
statsDF.drop(statsDF.columns[statsDF.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

# For each row we create a dictionary where key is column name and value is entry at that column and row
res = []
for i in range(len(statsDF.index)):
    curr = {}
    for col in statsDF.columns:
        curr[col] = statsDF.iloc[i][col]
    res.append(curr)

for k, v in res[0].items():
    print("Key: {} \nValue: {}\n".format(k, v))