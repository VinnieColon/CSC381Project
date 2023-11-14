# Imports 
import streamlit as st


# View for displaying multiselect for primary key
def selectPrimKey(df):

    primKey = st.multiselect("Select columns for Primary Key", df.columns)
    submitBtn = st.button("Submit")

    if submitBtn:
        st.session_state["primary_key"] = primKey