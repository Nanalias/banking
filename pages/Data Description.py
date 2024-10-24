import streamlit as st
st.header('Data Description on Banking Data')


import pandas as pd

#st.write(df.head())
st.caption("The first 5 rows of banking dataset were shown below")
df = pd.read_csv('banking.csv')
st.dataframe(df.head())

st.subheader("Banking Dataset Information")
st.text(f"Dimension of dataset: {df.ndim}") # show dimension
st.text(f"Shape of dataset: {df.shape}")  # Show rows and columns count
st.text(f"List of variables name in dataset: {df.columns}") # Show variables 
st.text(f"Range index of dataset: {df.index}")# Show range index 

import io
# Create a buffer to capture the output of df.info()
buffer = io.StringIO()
df.info(buf=buffer)
info = buffer.getvalue()

# Display df.info() output in Streamlit
st.subheader("DataFrame Information - Data Type, No of columns and rows")
st.text(info)