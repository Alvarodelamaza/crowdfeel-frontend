import streamlit as st
import datetime
import os
import pandas as pd
import numpy as np
import requests
import pydeck as pdk
import string

st.set_page_config(
     page_title="Crowdfeel app",
     page_icon="twitter",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://github.com/tjebbel/crowdfeel',
         'Report a bug': "https://github.com/tjebbel/crowdfeel",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )
'''
# Predict the mood and sentiment of your tweet in a location
'''


st.markdown('''
## Enter the details about your desired tweet
''')

date = st.date_input(' datetime', value=datetime.datetime(2022, 8, 1, 12, 10, 20))
time = st.time_input(' datetime', value=datetime.datetime(2022, 8, 31, 12, 10, 20))
hashtag = st.text_input(label='Enter #Hashtag')
location = st.text_input(label='Enter Location')
handle = st.text_input(label='Enter @Handle')
freetext = st.text_input(label='Enter Text')

st.markdown('''
## This slider allows the user to select a number of tweets
''')

tweet_count = st.slider('Select a tweet count', 1, 100, 5)

st.markdown('''
## Overall barometer of the mood for your tweet
''')
positive = 0.55
negative = 0.45
value = (positive / (positive + negative))
st.progress(value)


st.markdown('''
## Enter the details to compare the mood of your location 🔜
''')

col1, col2 = st.columns(2)
col1.markdown(''' ### Me... 🗺''')
location = col1.text_input('Location')

col2.markdown('''### You... 📍''')
destination = col2.text_input('Destination')

col1, col2, col3, col4 = st.columns(4)
col1.metric("Location: Positive tweets", "500", "+25%")
col2.metric("Location: Negative tweets", "500", "-25%")
col3.metric("Location: Change # of tweets", "+5%", "-4%")
col4.metric("Location: Change sentiment", "+5%", "-4%")


st.markdown('''
## Enter the details to compare the mood in radius from your location 🔜
''')


df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [52.442039, 4.829199],
    columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
     map_style=None,
     initial_view_state=pdk.ViewState(
         latitude=52.442039,
         longitude= 4.829199,
         zoom=11,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            coverage=1
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=200,
         ),
     ],
 ))

st.markdown('''
## Enter the details to compare the mood of your destination 🔜
''')

col1, col2, col3, col4 = st.columns(4)
col1.metric("Destination: Positive tweets", "500", "+25%")
col2.metric("Destination: Negative tweets", "500", "-25%")
col3.metric("Destination: Change # of tweets", "+5%", "-4%")
col4.metric("Destination: Change sentiment", "+5%", "-4%")

st.markdown('''
## Enter the details to compare the mood in your destination 🔜
''')

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [51.92442, 4.47773],
    columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
     map_style=None,
     initial_view_state=pdk.ViewState(
         latitude=51.92442,
         longitude= 4.47773,
         zoom=11,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            coverage=1
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=200,
         ),
     ],
 ))

st.markdown('''
## Enter the details to compare sentiment on tweets
''')
