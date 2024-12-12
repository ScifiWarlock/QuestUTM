import streamlit as st
import requests
import pandas as pd
import json
from streamlit_lottie import st_lottie
import os

file_path = os.getcwd() + '\Main Scene.json'

with open(file_path, "r") as file:
    url = json.load(file)

#st.title("VCHS WildfireQuest")

st_lottie(url,
          reverse=True,
          height=900,
          width=800,
          speed=1,
          loop=True,
          quality='high',
          key='logo')

table = requests.get("http://127.0.0.1:8000/table_send").json()

wypt_df = pd.DataFrame(table)
st.dataframe(wypt_df)
