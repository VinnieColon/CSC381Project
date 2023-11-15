#Imports
import streamlit as st
import pandas as pd
import numpy as np
from Helpers.distance_help import euclidean_distance, manhattan_distance
from Helpers.choose_prim_key import selectRow

#Page name
st.title("Choose Similar Combination Algorithm")
    
#If statement to ensure that the sure csv file has been uploaded
if "csv_data" in st.session_state:
    df = st.session_state["csv_data"].copy()
    enableDownloads = False

    #needs to be renamed
    #select boxes should be 'Manhattan' or 'Crow Flies/Euclidean'
    chooseAlg = st.selectbox("Choose Combo Algorithm", ["Euclidean", "Manhattan"])
    chooseAx1 = st.selectbox("Choose a column", df.select_dtypes('floating').columns)
    chooseAx2 = st.selectbox("Choose a column", df.select_dtypes('floating').columns)
    
    #Selecting the Key
    chooseKey =st.selectbox("Primary Key", st.session_state["row_keys"].keys())

    submitBtn = st.button("Submit Button")
    if submitBtn:
        chosenRow = selectRow(df, chooseKey)
        distances = []
        for i in range(len(df.index)):
            # Skip over the chosen row
            if i == st.session_state["row_keys"][chooseKey]:
                continue
            if chooseAlg == "Euclidean":
                sum = euclidean_distance
            else: 
                sum = manhattan_distance
        distances.append((sum))
    st.session_state["distance_{}".format(chooseKey)] = distances
            
else:
    st.subheader("No CSV data entered yet")