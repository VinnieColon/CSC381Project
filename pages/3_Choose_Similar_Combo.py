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
    chooseAx1 = st.multiselect("Choose Columns to Compare", df.select_dtypes('floating').columns)
    
    #Selecting the Key
    chooseKey =st.selectbox("Primary Key", st.session_state["row_keys"].keys())

    submitBtn = st.button("Submit Button")
    if submitBtn:
        chosenRow = selectRow(df, chooseKey)
        distances = []
        chosenEntry = df.iloc[st.session_state["row_keys"][chooseKey]]
        chosenDatapoint = []
        for cAx in chooseAx1:
            chosenDatapoint.append(chosenEntry[cAx])
        for i in range(len(df.index)):

            # Skip over the chosen row
            if i == st.session_state["row_keys"][chooseKey]:
                continue
            
            # Get Datapoint representing i-th row
            currDatapoint = []
            for cAx in chooseAx1:
                currDatapoint.append(df.iloc[i][cAx])

            # Compute distance between chosen row and i-th row
            if chooseAlg == "Euclidean":
                sum = euclidean_distance(chosenDatapoint, currDatapoint)
            else: 
                sum = manhattan_distance(chosenDatapoint, currDatapoint)
            distances.append(sum)

        # Write distances to session state
        st.session_state["distance_{}".format(chooseKey)] = distances
        st.write("Added to memory!")

        # Create and display dataframe containing
        display_df = st.session_state["csv_data"].copy()
        display_df = display_df.drop(st.session_state["row_keys"][chooseKey])
        display_df = display_df[st.session_state["primary_key"]]
        display_df["Distance"] = distances
        st.dataframe(display_df)
            
else:
    st.subheader("No CSV data entered yet")