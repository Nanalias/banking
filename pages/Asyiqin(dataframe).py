import streamlit as st
import pandas as pd

# Example DataFrame
st.sidebar.write('Dataset page')
df = pd.read_csv("banking.csv")

st.title("Banking Dataset")

# 1. Multiselect for columns
selected_columns = st.multiselect('Select columns to filter:', df.columns.tolist(), default=df.columns.tolist())

# Display the DataFrame with selected columns
if selected_columns:
    st.write(df[selected_columns])
else:
    st.write(df)