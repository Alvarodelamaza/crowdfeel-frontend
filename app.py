import streamlit as st

import datetime
import os
import requests

'''
# crowdfeel front

This front queries the Le Wagon [taxi fare model API]
(https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2)
'''

date = st.date_input(' datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
time = st.time_input(' datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
datetime = f'{date} {time}'
longitude = st.number_input('longitude', value=40.7614327)
latitude = st.number_input(' latitude', value=-73.9798156)
