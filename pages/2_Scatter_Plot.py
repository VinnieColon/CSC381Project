import streamlit as st
from matplotlib.figure import Figure

st.title("Scatter Plot")

if "csv_data" in st.session_state:
    df = st.session_state["csv_data"].copy()
    fig = Figure()
    enableDownloads = False
    with st.form("scatter_plot_form"):

        # Defining fields of form
        st.subheader("Pick Columns to be Plotted")
        xaxis = st.selectbox("Choose x-axis", df.select_dtypes('floating').columns)
        yaxis = st.selectbox("Choose y-axis", df.select_dtypes('floating').columns)
        submitted = st.form_submit_button()

        # Defining behavior upon submit
        if submitted:

            # Start rendering the downloads button
            enableDownloads = True

            # Defining matplotlib figure to be plotted
            plt = fig.subplots()
            plt.set_xlabel(xaxis)
            plt.set_ylabel(yaxis)
            plt.set_title("{} vs. {}".format(xaxis, yaxis))
            plt.scatter(df[xaxis], df[yaxis])

            # Plotting the figure
            st.pyplot(fig)

    # Button to download figure as png
    fig.savefig('downloads/dwn_fig.png', format='png')
    with open('downloads/dwn_fig.png', "rb") as file:
        btn = st.download_button('Download Plot', file, 'dwn_fig.png', 'image/png', disabled = not enableDownloads)

else:
    st.subheader("No CSV data entered yet")