import streamlit as st

import datetime
import os
import requests
import pandas as pd
import numpy as np
import pydeck as pdk

'''
# crowdfeel front

This front queries the Le Wagon [Crowdfeel API]

'''

date = st.date_input(' datetime', value=datetime.datetime(2022, 8, 1, 12, 10, 20))
time = st.time_input(' datetime', value=datetime.datetime(2022, 8, 31, 12, 10, 20))
datetime = f'{date} {time}'
longitude = st.number_input('longitude', value=40.7614327)
latitude = st.number_input(' latitude', value=-73.9798156)

st.markdown('''
## Enter the details to compare sentiment of your location to your destination 🔜
''')

col1, col2 = st.columns(2)
col1.markdown(''' ### Me... 🗺''')
location = col1.text_input('Location')

col2.markdown('''### You... 📍''')
destination = col2.text_input('Destination')

url_loc = f"https://maps.googleapis.com/maps/api/geocode/json?address={location.replace(' ','%20')}&key=AIzaSyBZaTwXWRvIM0INaGsrjU2-FvyQ2yCi5Q8"
response = requests.get(url_loc)
de_lat = response.json()['results'][0]['geometry']['location']['lat']
de_lng = response.json()['results'][0]['geometry']['location']['lng']
url_loc = f"https://maps.googleapis.com/maps/api/geocode/json?address={destination.replace(' ','%20')}&key=AIzaSyBZaTwXWRvIM0INaGsrjU2-FvyQ2yCi5Q8"
response_a = requests.get(url_loc)

dr_lat = response_a.json()['results'][0]['geometry']['location']['lat']
dr_lng = response_a.json()['results'][0]['geometry']['location']['lng']
pk_ad=response.json()['results'][0]["formatted_address"]
dr_ad=response_a.json()['results'][0]["formatted_address"]

col1.write(pk_ad)
col2.write(dr_ad)
