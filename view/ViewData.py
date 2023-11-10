import streamlit as st
import numpy as np
import pandas as pd

def view_data(givenChoiceDF = None):

    st.subheader("Data Table")

    if "csv_data" in st.session_state:
        if givenChoiceDF is not None:
            df = st.session_state["csv_data"].copy()[str(st.session_state["csv_indexes"].copy()[givenChoiceDF])]
        else:
            df = st.session_state["csv_data"].copy()["0"]
        st.dataframe(df)

        selectDF = st.selectbox("Select Dataframe to View", st.session_state["csv_indexes"].copy().keys())
        submitDF = st.button("Submit", on_click=view_data, args=selectDF)

    else:
        st.subheader("No CSV data entered yet")

