import streamlit as st
import pandas as pd
from view.ViewData import view_data

st.title("Upload a CSV")

up_file = st.file_uploader("Select a file")

if up_file is not None:
    df = pd.read_csv(up_file)
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    st.session_state["csv_data"] = df
    view_data()
elif "csv_data" in st.session_state:
    view_data()
