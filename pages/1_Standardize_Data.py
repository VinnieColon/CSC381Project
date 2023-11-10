import streamlit as st
from Helpers.stdrd_tableview import stdrd_tableview
import pandas as pd
from Helpers.save_df import saveDataframe

st.title("Standardize Columns of Data")

# If CSV data file has been entered in the current session
if "csv_data" in st.session_state:

    # Getting OG CSV file data as a dataframe
    df = st.session_state["csv_data"].copy()

    # Defining fields of form
    st.subheader("Choose Columns and Range")
    columns = st.multiselect("Choose One or More Columns", df.select_dtypes('floating').columns)
    ranges = st.selectbox("Choose a Range", ["0-1", "-1-1", "0-10", "1-10", "z"])
    pin_outliers = st.checkbox("Pin Outliers")
    submitted = st.button("Submit")
    if submitted:

        stdrd_tableview(df, columns, ranges, pin_outliers, submitted)

        # Text input field and button for saving the standardized CSV to the app's memory
        dfName = st.text_input("Enter name of data frame")
        
    elif "curr" in st.session_state:
        st.dataframe(st.session_state["curr"])

        # Text input field and button for saving the standardized CSV to the app's memory
        dfName = st.text_input("Enter name of data frame")
        if bool(dfName):
            saveDataframe(dfName, st.session_state["curr"].copy())

        
else:
    st.subheader("No CSV file has been entered")
                



