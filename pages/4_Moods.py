
from pickletools import read_bytes1
import streamlit as st
import datetime
#import time
import requests
import pandas as pd
import numpy as np
import pydeck as pdk
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
#import streamlit.components.v1 as components

import plotly.express as px

# Page configuration
st.set_page_config(
     page_title="CrowdFeel",
     page_icon="👥",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://github.com/Alvarodelamaza/crowdfeel',
         'Report a bug': "https://github.com/Alvarodelamaza/crowdfeel",
         'About': "## Population sentiment analysis using tweets \n Bootcamp project developed by: \n Alvaro de la Maza, Angelo Darriet, Beauregard Sangkala and Tjebbe Lodeizen"
     }
 )

# Title and subtitle
title='👥 Crowdfeel 👥'
subtitle="The tool to track people's sentiment through Twitter 💬"
st.markdown(f"<h1 style='text-align: center;font-size: 60px;'>{title}</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center;font-size: 35px;'>{subtitle}</h1>", unsafe_allow_html=True)


# Search form hashtag emotions
with st.form("search_form_emotions"):

    # Date filter
    st.markdown(f"<h1 style='text-align: center;font-size: 30px;'>When? 📆</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    date_start = col1.date_input(' From...', value=datetime.datetime(2022, 8, 1, 12, 10, 20))
    date_finish = col2.date_input(' ...to', value=datetime.datetime(2022, 8, 31, 12, 10, 20))

    # Hashtag filter
    st.markdown(f"<h1 style='text-align: center;font-size: 30px;'>Hashtag? #️⃣</h1>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    hashtag=col3.text_input(''' Hashtag you want to search ''')

    col11, col21 , col23,col34, col31 = st.columns(5)
    timeline=col23.checkbox('Show timeline', value=False)
    # Submit button
    col11, col21 , col23,col34, col31 = st.columns(5)
    submitted = col23.form_submit_button("Extract Sentiments from hashtag #️⃣ ")
    if submitted:

            # Print search filters
            st.write("Hashtag searched:  ", hashtag)

            # Call our API
            url=f'http://127.0.0.1:8000/predictemotionshas?hashtag={hashtag}'
            #Loading... spinner
            with st.spinner('Extracting emotions... 😃😭🤬😳'):
                res=requests.get(url).json()
                print(res)
                tweet=res['tweet']
                emotion=res['label']
            st.success('Emotions extracted succesfully!',icon='✅')

            emojy = []
            word = []
            for twee in tweet:
            # Set the emojis
                if emotion=='0':
                    emojy.append('😃')
                    word.append('Happy')
                elif emotion== '1':
                    emojy.append('🤬')
                    word.append('Hate')
                elif emotion=='2':
                    emojy.append('😍')
                    word.append('Love')
                elif emotion=='3':
                    emojy.append('😐')
                    word.append('Neutral')
                elif emotion=='4':
                    emojy.append('😭')
                    word.append('Sad')
                elif emotion=='5':
                    emojy.append('😲')
                    word.append('Surprise')
                else:
                    emojy.append('😱')
                    word.append('Worry')

            col1, col2 = st.columns(2)

            # Column #1 with random tweets and their labels
            with col1:
                with st.expander(" See random Tweets"):
                    for twee, emotion, labels in zip(tweet,emojy, word):
                        text=f'''{twee} is {labels}'''.replace("\n","")
                        text_html = f'<p style="font-family:sans-serif; font-size: 20px; border-radius: 25px; border: 2px solid; padding: 20px;">{text}</p>'
                        st.markdown(text_html, unsafe_allow_html=True)

            #Column #2 with charts
            with col2:
                st.bar_chart(data=emotion)
