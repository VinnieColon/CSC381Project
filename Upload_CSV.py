import streamlit as st
import pandas as pd
from view.ViewData import view_data
from Helpers.ident_rels import identRels
from Helpers.choose_prim_key import selectPrimKey

st.title("Upload a CSV")

up_file = st.file_uploader("Select a file")


# This if-statement executes when file is first uploaded
if up_file is not None:

    # Reading in the csv file as a df
    df = pd.read_csv(up_file)
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

    # Initializing session state variables
    st.session_state["csv_data"] = df
    st.session_state["csv_data_list"] = {"0": df}
    st.session_state["csv_indexes"] = {"OG data": 0}
    st.session_state["relationships"] = []

    # Selectbox to select df from app's memory and view it
    selectDF = st.selectbox("Select Dataframe to View", st.session_state["csv_indexes"].copy().keys())
    view_data(selectDF)

    # Displays form for identifying relationships and adding to memory
    identRels(df)

    # Form for entering a primary key
    selectPrimKey(df)


# This runs when csv has already been uploaded and user has left and returned to this page
elif "csv_data" in st.session_state:
    # Selectbox to select df from app's memory and view it
    selectDF = st.selectbox("Select Dataframe to View", st.session_state["csv_indexes"].copy().keys())
    view_data(selectDF)

    # Get df indicated by selectDF from the app's memory
    dfIdx = str(st.session_state["csv_indexes"][selectDF])
    df = st.session_state["csv_data_list"][dfIdx].copy()

    # Displays form for identifying relationships and adding to memory
    identRels(df)

    # Form for entering a primary key
    selectPrimKey(df)