import streamlit as st
from min_max_scale import stdDF
import pandas as pd

st.title("Standardize Columns of Data")

# If CSV data file has been entered in the current session
if "csv_data" in st.session_state:

    # Getting OG CSV file data as a dataframe
    df = st.session_state["csv_data"].copy()

    with st.form("std_form"):

        # Defining fields of form
        st.subheader("Choose Columns and Range")
        columns = st.multiselect("Choose One or More Columns", df.select_dtypes('floating').columns)
        ranges = st.selectbox("Choose a Range", ["0-1", "-1-1", "0-10", "1-10", "z"])
        submitted = st.form_submit_button()

        # Defining behavior of app upon submission of form
        if submitted and columns is not None:

            # Getting a new data frame from OG with chosen columns standardized to desired range
            curr = stdDF(df, columns, ranges)

            # Displaying the resulting data table
            st.subheader("Standardized Data:")
            st.dataframe(curr)
        
else:
    st.subheader("No CSV file has been entered")
                
