# This displays the data table with the user input columns and range
# Also stores the resulting dataframe to "curr" in st.session_state

# Imports
import streamlit as st
from Helpers.min_max_scale import stdDF

def stdrd_tableview(df, columns, ranges, pin_outliers, submitted):
    # Defining behavior of app upon submission of form
    if submitted and columns is not None:

        # Getting a new data frame from OG with chosen columns standardized to desired range
        curr = stdDF(df, columns, ranges, pin_outliers)
        st.session_state["curr"] = curr

        # Displaying the resulting data table
        st.subheader("Standardized Data:")
        st.dataframe(curr)