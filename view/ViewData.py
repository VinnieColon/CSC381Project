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

    else:
        st.subheader("No CSV data entered yet")

