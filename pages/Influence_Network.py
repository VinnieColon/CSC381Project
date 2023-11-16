# influence_network_page.py
import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def create_influence_network(df, relationships):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges based on relationships
    for cause, effect in relationships:
        G.add_edge(cause, effect)

    return G

def influence_network_page():
    st.title("Influence Network")

    # Check if a CSV file has been entered
    if "csv_data" not in st.session_state:
        st.subheader("No CSV data entered yet.")
        return

    # Select DataFrame
    selectDF = st.selectbox("Select a dataframe", st.session_state["csv_indexes"].copy().keys())
    df = st.session_state["csv_data_list"].copy()[str(st.session_state["csv_indexes"][selectDF])]

    # Display relationships from memory
    relationships = st.session_state.get("relationships", [])
    st.subheader("Current Relationships:")
    for cause, effect in relationships:
        st.write(f"{cause} influences {effect}")

    # Create influence network
    G = create_influence_network(df, relationships)

    # Draw and display the network
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', arrowsize=15)
    st.pyplot(plt)

if __name__ == "__main__":
    influence_network_page()
