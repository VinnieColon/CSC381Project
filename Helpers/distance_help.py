#imports
import streamlit as st
import numpy as np

#Finding the Euclidean
def euclidean_distance(selected1, selected2):
    sum = 0
    for i in range(2):
        sum += (selected1[i] - selected2[i]) ** 2

    return np.sqrt(sum)

#Finding Manhattan
def manhattan_distance(selected1, selected2):
    sum = 0
    for i in range(2):
        sum += abs(selected1[i] - selected2[i])

    return sum

#selecting the row
def selectRow(df, chooseKey):
    idx = st.session_state["row_keys"].copy()[chooseKey]
    return df.iloc[idx]