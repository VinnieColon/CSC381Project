import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from scipy.stats import zscore


# Defining a function that performs min-max standardization
def minMaxScale(df: pd.DataFrame, col: str, low = 0, high = 1, pin_outliers = False):
    data = df[col].to_numpy().reshape((len(df.index), 1))
    scaler = MinMaxScaler(feature_range=(low, high))
    scaler.fit(data)
    res = list(np.array(scaler.transform(data)).flatten())
    if pin_outliers:
        resMean = np.mean(res)
        res3Std = np.std(res) * 3
        for i in range(len(res)):
            diff = res[i] - resMean
            if diff >= res3Std:
                res[i] = high
            elif diff <= -1 * res3Std:
                res[i] = low

    return res


# Defining a function that takes a data frame, a list of columns, and the range to which
# those columns will be standardized, returns df with standardized columns
def stdDF(df: pd.DataFrame, columns, ranges: str, pin_outliers):
    if ranges == 'z':
        for col in columns:
            curr = zscore(df[col])
            df[col] = curr
    else:
        # Getting low and high bound of range as integers
        low, high = 0, 0
        if ranges[0] == '-':
            low, high = -1, 1
        else:
            splitRange = ranges.split('-')
            low = int(splitRange[0])
            high = int(splitRange[1])
        
        # Performing min-max scaling on chosen columns
        for col in columns:
            curr = minMaxScale(df, col, low, high, pin_outliers)
            df[col] = curr

    return df