# This function is used to save an augmented dataframe to the app's memory

# Imports
import streamlit as st

# Functionality for saving dataframe to app's memory
def saveDataframe(name, df):
    if name == "":
        st.write("You must enter a name to save the data frame!")
    elif name in st.session_state["csv_indexes"].keys():
        st.write("That name is already taken!")
    else:
        numDfs = len(st.session_state["csv_data"].keys()) + 1
        st.session_state["csv_indexes"][name] = numDfs
        st.session_state["csv_data"][str(numDfs)] = df
        st.write("Data frame saved to app's memory!")