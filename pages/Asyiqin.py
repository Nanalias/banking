import streamlit as st
import plotly.express as px
import pandas as pd

# Load the data
df = pd.read_csv("banking.csv")

# Set the title of the app
st.header("Analysis based on Categorical Values")

# Identify categorical columns
categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()

# Create a selectbox for users to choose a categorical column for analysis
column_to_analyze = st.selectbox("Select a categorical column to analyze:", categorical_columns)

# Create columns for layout
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"Unique Value Counts in '{column_to_analyze}'")
    # Display unique value counts for the selected column
    value_counts = df[column_to_analyze].value_counts()
    st.write(value_counts)

with col2:
    # Check if the selected column has enough unique values for a pie chart
    if value_counts.shape[0] > 1:  # Only create a pie chart if more than 1 unique value
        # Group by the selected column to get the count of each unique value
        unique_counts = df[column_to_analyze].value_counts().reset_index()
        unique_counts.columns = [column_to_analyze, 'Count']

        # Create a pie chart using Plotly Express
        fig = px.pie(unique_counts, names=column_to_analyze, values='Count', title=f'{column_to_analyze} Distribution')

        # Display the pie chart in Streamlit
        st.plotly_chart(fig)
    else:
        st.write("Not enough unique values to create a pie chart.")
