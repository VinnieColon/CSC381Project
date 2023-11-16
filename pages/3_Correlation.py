import streamlit as st
import pandas as pd

def correlation_page():
    st.title("Column Correlation")

    # Check if a CSV file has been entered
    if "csv_data" not in st.session_state:
        st.subheader("No CSV data entered yet.")
        return

    # Select DataFrame
    selectDF = st.selectbox("Select a dataframe", st.session_state["csv_indexes"].copy().keys())
    df = st.session_state["csv_data_list"].copy()[str(st.session_state["csv_indexes"][selectDF])]

    # Select columns for correlation
    st.subheader("Choose Columns for Correlation")
    selected_columns = st.multiselect("Select columns", df.columns)
    
    # Check if at least two columns are selected
    if len(selected_columns) < 2:
        st.subheader("Please select at least two columns for correlation.")
        return

    # Calculate correlation matrix and coefficients
    correlation_matrix = df[selected_columns].corr()
    coefficients = []

    for col1 in selected_columns:
        for col2 in selected_columns:
            if col1 != col2:
                correlation_coefficient = df[col1].corr(df[col2])
                coefficients.append((col1, col2, correlation_coefficient))

    # Display correlation matrix as a heatmap
    st.write("Correlation Matrix:")
    st.write(correlation_matrix)

    # Display individual correlation coefficients
    st.subheader("Correlation Coefficients")
    for col1, col2, coefficient in coefficients:
        st.write(f"{col1} and {col2}: {coefficient:.4f}")

if __name__ == "__main__":
    correlation_page()

