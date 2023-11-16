#Imports 
import streamlit as st

def high_good(df):
    chooseCol = st.selectbox ("Choose Column", df.columns)
    high_good = st.selectbox("High is good?", ["Yes", "No"])

    #button
    submitBtn = st.button("Enter")
    if submitBtn:
        if high_good == "Yes":
            st.session_state["good_or_bad"][chooseCol] = True
        else:
            st.session_state["good_or_bad"][chooseCol] = False
        st.write("Added to memory")