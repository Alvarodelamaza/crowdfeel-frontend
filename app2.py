import streamlit as st
import datetime
import time
import requests
import pandas as pd
import numpy as np
import pydeck as pdk
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(
     page_title="CrowdFeel",
     page_icon="👥",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://github.com/Alvarodelamaza/crowdfeel',
         'Report a bug': "https://github.com/Alvarodelamaza/crowdfeel",
         'About': "## Population sentiment analysis using tweets \n Bootcamp project developed by "
     }
 )

'''
# 👥 Crowdfeel

## The tool to track people's sentiment through Twitter 💬

'''
with st.form("search_form"):
    st.markdown(''' ### When? 📆''')
    col1, col2 = st.columns(2)
    date_start = col1.date_input(' From...', value=datetime.datetime(2022, 8, 1, 12, 10, 20))
    date_finish = col2.date_input(' ...to', value=datetime.datetime(2022, 8, 31, 12, 10, 20))


    st.markdown(''' ### Where? 🗺''')
    col3, col4 = st.columns(2)
    location=col3.text_input(''' City''')
    radius=col4.slider('''Radius (km)''',min_value=1, max_value=50)
    submitted = st.form_submit_button("Extract Sentiments from location")
    if submitted:
            st.write("Location:", location, ",radius:", radius)
            url=f'http://127.0.0.1:8000/predictbeta?distance={radius}&location={location}'
            with st.spinner('Extracting emotions😃😭🤬😳...'):
                happiness=np.round(requests.get(url).json()['happiness'],2)
            st.success('Done!')
            if happiness >50:
                emojy='😃'
            else:
                emojy='😭'
            f''' ## The level of happiness of **{location}** is {happiness}  {emojy}'''

            emotions=np.array([happiness,100-happiness])
            my_labels=['Happy 😃','Sad 😭']
            colors=['#95CD41','#FA877F']

            plt.figure(figsize=(2, 2))
            fig, ax = plt.subplots()

            ax.pie(emotions,labels=my_labels,colors=colors)

            st.pyplot(fig)
with st.form("search_form_hastga"):
    st.markdown(''' ### When? 📆''')
    col1, col2 = st.columns(2)
    date_start = col1.date_input(' From...', value=datetime.datetime(2022, 8, 1, 12, 10, 20))
    date_finish = col2.date_input(' ...to', value=datetime.datetime(2022, 8, 31, 12, 10, 20))


    st.markdown(''' ### Hashtag? #️⃣ ''')
    col3, col4 = st.columns(2)
    hashtag=col3.text_input(''' Hashtag ''')

    submitted = st.form_submit_button("Extract Sentiments from hashtag")
    if submitted:
            st.write("Hashtag:", hashtag)
            url=f'http://127.0.0.1:8000/predicthasacc?hashtag={hashtag}'
            with st.spinner('Extracting emotions😃😭🤬😳...'):
                res=requests.get(url).json()
                happiness=np.round(res['happiness'],2)
                tweet=res['tweet']
                label=res['label']
            st.success('Done!')
            if happiness >50:
                emojy='😃'
            else:
                emojy='😭'

            if label==1:
                label='✅ Positive'
            else:
                label='❌ Negative'
            f''' ## The emotions of #**{hashtag}** is {happiness}  {emojy}'''
            f'''## An example...{tweet}, which is {label}'''
            emotions=np.array([happiness,100-happiness])
            my_labels=['Happy 😃','Sad 😭']
            colors=['#95CD41','#FA877F']

            plt.figure(figsize=(2, 2))
            fig, ax = plt.subplots()

            ax.pie(emotions,labels=my_labels,colors=colors)

            st.pyplot(fig)




#url_loc = f"https://maps.googleapis.com/maps/api/geocode/json?address={location.replace(' ','%20')}&key=AIzaSyBZaTwXWRvIM0INaGsrjU2-FvyQ2yCi5Q8"
#response = requests.get(url_loc)

#de_lat = response.json()['results'][0]['geometry']['location']['lat']
#de_lng = response.json()['results'][0]['geometry']['location']['lng']
#url_loc = f"https://maps.googleapis.com/maps/api/geocode/json?address={destination.replace(' ','%20')}&key=AIzaSyBZaTwXWRvIM0INaGsrjU2-FvyQ2yCi5Q8"
#response_a = requests.get(url_loc)

#dr_lat = response_a.json()['results'][0]['geometry']['location']['lat']
#dr_lng = response_a.json()['results'][0]['geometry']['location']['lng']
#pk_ad=response.json()['results'][0]["formatted_address"]
#dr_ad=response_a.json()['results'][0]["formatted_address"]
#col1.write(pk_ad)
#col2.write(dr_ad)
