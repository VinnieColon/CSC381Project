import streamlit as st
import pandas as pd
import numpy as np
from Helpers.distance_help import distance_help

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


    
else:
    st.subheader("No CSV data entered yet")