import streamlit as st
import datetime
import os
import requests

st.set_page_config(
     page_title="Crowdfeel",
     page_icon="🫶",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://github.com/Alvarodelamaza/crowdfeel-frontend',
         'Report a bug': "https://github.com/Alvarodelamaza/crowdfeel-frontend",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )
'''
# Predict your tweet sentiment
'''

st.markdown('''
## Enter the details about your desired ride 🔜
''')

date = st.date_input(' datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
time = st.time_input(' datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
hashtag = st.text_input(label='Enter #Hashtag')
location = st.text_input(label='Enter Location')
handle = st.text_input(label='Enter @Handle')
freetext = st.text_input(label='Enter Text')
