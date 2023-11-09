import streamlit as st
import numpy as np
import pandas as pd


def responseAddIO(inp,outp):
    if inp is not None and outp is not None:
        st.session_state["Inputs"]=inp
        st.session_state["Outputs"]=outp
    else:
        st.write("No Inputs or Outputs selected")


def view_data():

    st.subheader("Data Table")

    if "csv_data" in st.session_state:
        df = st.session_state["csv_data"].copy()
        st.dataframe(df)

        inputs= st.multiselect("Inputs",df.columns)
        outputs= st.multiselect("Outputs",df.columns)
        AddIO = st.button("Add Input/Outputs",on_click=responseAddIO)

    else:
        st.subheader("No CSV data entered yet")

