import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('banking.csv')

# Display the dataframe
#st.dataframe(df)


st.subheader("This is the Banking Distribution Report")
    
    # Selectbox for attribute selection
attribute = st.selectbox("Please select the attribute:", ['age', 'Job vs Education Level', 'Marital Status and Loan'])

    # Visualization based on selected attribute
if attribute == 'age':
    plt.figure(figsize=(10, 6))
    sns.histplot(df['age'], bins=30, kde=True)  # Histogram with kernel density estimate
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    st.pyplot(plt)

elif attribute == 'Job vs Education Level':
    plt.figure(figsize=(12, 6))
    ax = sns.countplot(data=df, x='job', hue='education', palette='Set2')  # Count plot with hue
    plt.title('Job vs Education Level')
    plt.xlabel('Job')
    plt.ylabel('Count')
    plt.xticks(rotation=45)  # Rotate x labels for better readability

    st.pyplot(plt)

elif attribute == 'Marital Status and Loan':
    plt.figure(figsize=(10, 6))
    ax = sns.countplot(data=df, x='marital', hue='loan', palette='Set1')  # Count plot with hue
    plt.title('Marital Status and Loan')
    plt.xlabel('Marital Status')
    plt.ylabel('Count')

    # Add count values to each bar
    for p in ax.patches:
        ax.text(p.get_x() + p.get_width() / 2., p.get_height(), str(int(p.get_height())),
                ha="center", va="bottom", size=8)

    st.pyplot(plt)