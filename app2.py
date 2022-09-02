from pickletools import read_bytes1
import streamlit as st
import datetime
import time
import requests
import pandas as pd
import numpy as np
import pydeck as pdk
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components


st.set_page_config(
     page_title="CrowdFeel",
     page_icon="👥",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://github.com/Alvarodelamaza/crowdfeel',
         'Report a bug': "https://github.com/Alvarodelamaza/crowdfeel",
         'About': "## Population sentiment analysis using tweets \n Bootcamp project developed by: \n Beauregard Alexander, Tjebbe Lodeizen, Angelo Darriet and Alvaro de la Maza"
     }
 )

title='👥 Crowdfeel'
subtitle="The tool to track people's sentiment through Twitter 💬"
st.markdown(f"<h1 style='text-align: center;font-size: 60px;'>{title}</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center;font-size: 35px;'>{subtitle}</h1>", unsafe_allow_html=True)

with st.form("search_form"):
    st.markdown(f"<h1 style='text-align: center;font-size: 30px;'>When? 📆</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    date_start = col1.date_input(' From...', value=datetime.datetime(2022, 8, 1, 12, 10, 20))
    date_finish = col2.date_input(' ...to', value=datetime.datetime(2022, 8, 31, 12, 10, 20))



    st.markdown(f"<h1 style='text-align: center;font-size: 30px;'>Where? 🗺</h1>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    location=col3.text_input(''' City''')
    radius=col4.slider('''Radius (km)''',min_value=1, max_value=50)

    submitted = st.form_submit_button("Extract Sentiments from location 🌍")


    if submitted:
            st.write("Location:", location, ",radius:", radius)
            url=f'http://127.0.0.1:8000/predictbeta?distance={radius}&location={location}'
            with st.spinner('Extracting emotions😃😭🤬😳...'):
                res1=requests.get(url).json()
                print('✅request made')
                happiness=np.round(res1['happiness'],2)
                tweet=res1['tweet']
                labels=res1['label']
            st.success('Done!')
            if happiness >50:
                emojy='😃'
            else:
                emojy='😭'
            label_text=[]
            color=[]
            for label in labels:
                if label==1:
                    label_text.append('✅ Positive')
                    color.append('Green')
                else:
                    label_text.append('❌ Negative')
                    color.append('Red')
            f''' ## The level of happiness of **{location}** is {happiness}  {emojy}'''
            col1, col2 = st.columns(2)
            with col1:
                with st.expander(" See random Tweets"):
                    for twee , label, color in zip(tweet,label_text,color):
                        text=f'''{twee} **is** {label}'''
                        text_html = f'<p style="font-family:sans-serif; color:{color}; font-size: 20px;">{text}</p>'
                        st.markdown(text_html, unsafe_allow_html=True)

            with col2:
                emotions=np.array([happiness,100-happiness])
                my_labels=['Happy 😃','Sad 😭']
                colors=['#95CD41','#FA877F']


                fig, ax = plt.subplots()

                ax.pie(emotions,labels=my_labels,colors=colors)

                st.pyplot(fig)
with st.form("search_form_hastga"):

    st.markdown(f"<h1 style='text-align: center;font-size: 30px;'>When? 📆</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    date_start = col1.date_input(' From...', value=datetime.datetime(2022, 8, 1, 12, 10, 20))
    date_finish = col2.date_input(' ...to', value=datetime.datetime(2022, 8, 31, 12, 10, 20))


    st.markdown(f"<h1 style='text-align: center;font-size: 30px;'>Hashtag? #️⃣</h1>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    hashtag=col3.text_input(''' Hashtag ''')

    submitted = st.form_submit_button("Extract Sentiments from hashtag #️⃣ ")
    if submitted:
            st.write("Hashtag:", hashtag)
            url=f'http://127.0.0.1:8000/predicthasacc?hashtag={hashtag}'
            with st.spinner('Extracting emotions😃😭🤬😳...'):
                res=requests.get(url).json()
                happiness=np.round(res['happiness'],2)
                tweet=res['tweet']
                labels=res['label']
            st.success('Done!',icon='✅')
            if happiness >50:
                emojy='😃'
            else:
                emojy='😭'
            label_text=[]
            color=[]
            for label in labels:
                if label==1:
                    label_text.append('✅ Positive')
                    color.append('Green')
                else:
                    label_text.append('❌ Negative')
                    color.append('Red')
            f''' ## The emotions of #**{hashtag}** is {happiness}  {emojy}'''
            col1, col2 = st.columns(2)
            with col1:
                with st.expander(" See random Tweets"):
                    for twee , label, color in zip(tweet,label_text,color):
                        text=f'''{twee} **is** {label}'''
                        text_html = f'<p style="font-family:sans-serif; color:{color}; font-size: 20px;">{text}</p>'
                        st.markdown(text_html, unsafe_allow_html=True)

            with col2:
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
