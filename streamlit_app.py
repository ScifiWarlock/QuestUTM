import streamlit as st
import requests
import pandas as pd
import json
#from streamlit_lottie import st_lottie
import os
import numpy as np
#import numpy
#import streamlit.components.v1 as components
import base64

np.bool = np.bool_
np.object = object

file_path = os.getcwd() + '/mainscene_6ac041e0.mp4'

#with open(file_path, "r") as file:
    #url = json.load(file)

#st.title("VCHS WildfireQuest")

# st_lottie(url,
#           reverse=True,
#           height=850,
#           width=700,
#           speed=1,
#           loop=True,
#           quality='high',
#           key='logo')

#st.video(file_path, format="video/mp4")

file = open(r"mainscene_2cb7447e.gif", 'rb')
contents = file.read()
data_url = base64.b64encode(contents).decode("utf-8")
file.close()
st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="GIF" style="width:100%;max-width:800px">',unsafe_allow_html = True)

# HTML to render the Lottie animation
# lottie_html = f"""
# <!DOCTYPE html>
# <html>
# <head>
#   <script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.9.6/lottie.min.js"></script>
# </head>
# <body>
#   <div id="lottie-animation" style="width: 100%; height: 400px; margin: 0 auto;"></div>
#   <script>
#     var animation = lottie.loadAnimation({{
#       container: document.getElementById('lottie-animation'),
#       renderer: 'svg',
#       loop: true,
#       autoplay: true,
#       animationData: {url}
#     }});
#   </script>
# </body>
# </html>
# """

# Embed the Lottie animation in Streamlit
#st.components.v1.html(lottie_html, height=850)


table = requests.get("http://127.0.0.1:8000/table_send").json()

wypt_df = pd.DataFrame(table)
st.dataframe(wypt_df)

# csv_download = wypt_df.to_csv().encode("utf-8")

# st.download_button(
#     label="Download data as CSV",
#     data=csv_download,
#     file_name="large_df.csv",
#     mime="text/csv",
# )

if st.button(label="Refresh data", key="refresh"):
    st.write("Press cmd+r lmaoo")

#st.map(data=wypt_df.loc[:2], use_container_width=True)
