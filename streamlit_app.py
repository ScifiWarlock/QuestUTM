import streamlit as st
import requests
import pandas as pd
import json
from streamlit_lottie import st_lottie
import os

file_path = os.path.join(os.getcwd(), 'logo.json')

with open(file_path, "r") as file:
    url = json.load(file)

st.markdown(
    """
    <style>
    .lottie-container {
        width: 400px; 
        height: 800px; 
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown('<div class="lottie-container">', unsafe_allow_html=True)
st_lottie(url, 
          reverse=True,
          speed=1,
          loop=True,
          quality='high',
          key='logo')
st.markdown('</div>', unsafe_allow_html=True)


table = requests.get("http://127.0.0.1:8000/table_send").json()
wypt_df = pd.DataFrame(table)
st.dataframe(wypt_df)
