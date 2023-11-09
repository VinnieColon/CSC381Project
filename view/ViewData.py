import streamlit as st
import numpy as np
import pandas as pd

def view_data():

    st.subheader("Data Table")

    if "csv_data" in st.session_state:
        df = st.session_state["csv_data"].copy()
        st.dataframe(df)
    else:
        st.subheader("No CSV data entered yet")

