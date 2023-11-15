#Imports
import streamlit as st
import pandas as pd
import numpy as np
from Helpers.distance_help import euclidean_distance, manhattan_distance
from Helpers.choose_prim_key import selectRow

#Page name
st.title("Choose Similar Combination Algorithm")
    
#If statement to ensure that the sure csv file has been uploaded
if "row_keys" not in st.session_state:
    st.subheader("No Primary Key Given")
elif "csv_data" in st.session_state:
    df = st.session_state["csv_data"].copy()
    enableDownloads = False

    #needs to be renamed
    #select boxes should be 'Manhattan' or 'Crow Flies/Euclidean'
    chooseAlg = st.selectbox("Choose Combo Algorithm", ["Euclidean", "Manhattan"])
    chooseAx1 = st.selectbox("Choose 1st column", df.select_dtypes('floating').columns)
    chooseAx2 = st.selectbox("Choose 2nd column", df.select_dtypes('floating').columns)
    
    #Selecting the Key
    chooseKey =st.selectbox("Primary Key", st.session_state["row_keys"].keys())

    submitBtn = st.button("Submit Button")
    if submitBtn:
        chosenRow = selectRow(df, chooseKey)
        distances = []
        chosenEntry = df.iloc[st.session_state["row_keys"][chooseKey]]
        chosenDatapoint = [chosenEntry[chooseAx1], chosenEntry[chooseAx2]]
        for i in range(len(df.index)):
            # Skip over the chosen row
            if i == st.session_state["row_keys"][chooseKey]:
                continue
            
            currDatapoint = [df.iloc[i][chooseAx1], df.iloc[i][chooseAx2]]
            if chooseAlg == "Euclidean":
                sum = euclidean_distance(chosenDatapoint, currDatapoint)
            else: 
                sum = manhattan_distance(chosenDatapoint, currDatapoint)
            distances.append(sum)

        # Write distances to session state
        st.session_state["distance_{}".format(chooseKey)] = distances
        st.write("Added to memory!")
            
else:
    st.subheader("No CSV data entered yet")