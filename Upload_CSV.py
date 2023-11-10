import streamlit as st
import pandas as pd
from view.ViewData import view_data

st.title("Upload a CSV")

up_file = st.file_uploader("Select a file")

if up_file is not None:
    df = pd.read_csv(up_file)
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    st.session_state["csv_data"] = df
    st.session_state["csv_data_list"] = {"0": df}
    st.session_state["csv_indexes"] = {"OG data": 0}
    selectDF = st.selectbox("Select Dataframe to View", st.session_state["csv_indexes"].copy().keys())
    view_data(selectDF)
elif "csv_data" in st.session_state:
    selectDF = st.selectbox("Select Dataframe to View", st.session_state["csv_indexes"].copy().keys())
    view_data(selectDF)
