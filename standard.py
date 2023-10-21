# This file will contain the code for standardization of columns in data table

# Imports
from scipy.stats import zscore
import pandas

# Reading in stats.csv as dataframe
statsDF = pandas.read_csv('stats.csv')

# Standardizing the xwoba column by using ZScore and outputting first few rows of result
xwobaZScore = pandas.DataFrame({
    'xwoba': statsDF['xwoba'],
    'zscores': zscore(statsDF['xwoba'])
})
print(xwobaZScore.head())