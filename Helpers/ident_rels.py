# This is a helper view to make reduce redundant code in Upload_CSV.py

# Imports
import streamlit as st

# Function diplaying selectboxes and button
def identRels(df):

    # Subheader for the view
    st.subheader("Identify Relationships")

    # Selectboxes for cause and effect relationship between 2 columns
    cause = st.selectbox("Choose Cause", df.columns)
    effect = st.selectbox("Choose Effect", df.columns)

    # Button to submit this relationship to the app's memory
    submitRel = st.button("Submit")
    if submitRel:
        st.session_state["relationships"].append([cause, effect])
        st.write("Relationship added to memory!")

    # Button that allows user to clear memory of all saved relationships
    clearRels = st.button("Clear Mem")
    if clearRels:
        st.session_state["relationships"] = []
        st.write("Memory Cleared!")