# Imports 
import streamlit as st


# View for displaying multiselect for primary key
def selectPrimKey(df):

    st.subheader("Select Primary Key")

    primKey = st.multiselect("Select columns for Primary Key", df.columns)
    submitBtn = st.button("Submit Primary Key")

    if submitBtn:
        st.session_state["primary_key"] = primKey
        rowSelect = {}
        for i in range(len(df.index)):
            currdf = df.iloc[i]
            key = ""
            for col in primKey:
                key += "{}_".format(currdf[col])
            rowSelect[key] = i
        st.session_state["row_keys"] = rowSelect
        st.write("Primary Key Saved!")
                


# Given a dataframe and a key for a row it will return that row
def selectRow(df, chosenRow):
    idx = st.session_state["row_keys"].copy()[chosenRow]
    return df.iloc[idx]