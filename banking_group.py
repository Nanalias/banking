# CREATING MULTIPAGES
import streamlit as st
st.set_page_config(
    page_title="BANKING_GROUP"
    )

st.markdown('# BANKING DATA')
from PIL import Image
im = Image.open('banking.png.png')
st.image(im)


st.subheader('EXPLANATION NEEDED FOR BANKING DATASET - WHAT? WHERE? WHO?ETC')
st.sidebar.write("Main Page")

import pandas as pd
df = pd.read_csv('banking.csv')
st.caption("The banking dataset is shown below")
st.dataframe(df)