
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Green Hydrogen Cost Dashboard")

st.write("Upload your CSV to analyze hydrogen cost scenarios.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())
    fig = px.line(df, x=df.columns[0], y=df.columns[1])
    st.plotly_chart(fig)
