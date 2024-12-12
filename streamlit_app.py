import streamlit as st
import requests
import pandas as pd

st.title("QuestUTM: WildfireQuest's intranet traffic management system")

table = requests.get("http://127.0.0.1:8000/table_send").json()

wypt_df = pd.DataFrame(table)
st.dataframe(wypt_df)
