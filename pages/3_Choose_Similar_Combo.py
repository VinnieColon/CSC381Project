import streamlit as st
import pandas as pd

#Page name
st.title("Choose Similar Combination Algorithm")

#If statement to ensure that the sure csv file has been uploaded
if "csv_data" in st.session_state:
    df = st.session_state["csv_data"].copy()
    

    #Euclidean algorithm formula
    #a, b, x, and y need to be replaced with proper inputs
    def euclidean_distance(x,y):
        sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

    #needs to be renamed
    #select boxes should be 'Manhattan' or 'Crow Flies/Euclidean'
    xaxis = st.selectbox("Choose x-axis", df.select_dtypes('floating').columns)
    yaxis = st.selectbox("Choose y-axis", df.select_dtypes('floating').columns)
    


else:
    st.subheader("No CSV data entered yet")