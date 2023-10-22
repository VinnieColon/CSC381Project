# This file will contain the code for standardization of columns in data table


# Imports
from pandas.core.frame import DataFrame
from scipy.stats import zscore
import pandas
import numpy as np


# Reading in stats.csv as dataframe
statsDF = pandas.read_csv('stats.csv')


# Standardizing the xwoba column by using ZScore and outputting first few rows of result
xwobaZScore = pandas.DataFrame({
    'xwoba': statsDF['xwoba'],
    'zscores': zscore(statsDF['xwoba'])
})

# Uncomment Following lines to see example
#print("Standardized xwoba to ZScores")
#print(xwobaZScore.head())


# This function will standardize data to range given by arguments low and high
# Min in OG data will equal low and Max will equal high
def scaleData(data: np.array, low, high):
    res = []
    min, max = np.min(data), np.max(data)
    diff = max - min
    for d in data:
        if d == min:
            res.append(low)
        elif d == max:
            res.append(high)
        else:
            curr = (d-min)/diff
            res.append(low + curr * (high - low))
    
    return res


# Standardizing the xwoba column to values between 0 and 1 using scaleData function
stdZeroOne = scaleData(statsDF['xwoba'].to_numpy(), 0, 1)
ogData = statsDF['xwoba'].to_list()

# Uncomment the following loop to see the examples (WARNING: prints ~300 lines to terminal)
#for i in range(len(stdZeroOne)):
#    print("OG: {}      New: {}\n".format(ogData[i], stdZeroOne[i]))
