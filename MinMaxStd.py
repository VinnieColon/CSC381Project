import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np


# Defining a function that performs min-max standardization
def minMaxScale(df: pd.DataFrame, low = 0, high = 1):
    data = df['xwoba'].to_numpy().reshape((len(df.index), 1))
    scaler = MinMaxScaler(feature_range=(low, high))
    scaler.fit(data)
    res = list(np.array(scaler.transform(data)).flatten())
    return res


# Example
""" df = pd.read_csv('static/data/stats.csv')
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
exRes = minMaxScale(df)
print(exRes) """