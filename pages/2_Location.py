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
#import streamlit.components.v1 as components

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
subtitle="The tool to track the sentiment in a location through Twitter 💬"
st.markdown(f"<h1 style='text-align: center;font-size: 60px;'>{title}</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center;font-size: 35px;'>{subtitle}</h1>", unsafe_allow_html=True)

# Location Form
with st.form("search_form location"):

    # Date filter
    st.markdown(f"<h1 style='text-align: center;font-size: 30px;'>When? 📆</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    date_start = col1.date_input(' From...', value=datetime.datetime(2022, 8, 1, 12, 10, 20))
    date_finish = col2.date_input(' ...to', value=datetime.datetime(2022, 8, 31, 12, 10, 20))

    # Location filter
    st.markdown(f"<h1 style='text-align: center;font-size: 30px;'>Where? 🗺</h1>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    location=col3.text_input(''' City''')
    radius=col4.slider('''Radius (km)''',min_value=1, max_value=50)

    # Submit button
    col11, col21 , col23,col34, col31 = st.columns(5)

    submitted = col23.form_submit_button("Extract Sentiments from location 🌍")
    if submitted:
            # Print search filters
            st.write("Location:", location, ",radius:", radius)
            # Call our API
            url=f'https://crowfeel-img-h5bk6vemiq-ez.a.run.app/predictbeta?distance={radius}&location={location}'

           #Loading... spinner
            with st.spinner('Extracting emotions... 😃😭🤬😳'):
                res1=requests.get(url).json()
                print('✅request made')
                happiness=np.round(res1['happiness'],2)
                tweet=res1['tweet']
                labels=res1['label']
            st.success('Sentiments extracted succesfully!',icon='✅')

            # Set the emojys
            if happiness >50:
                emojy='😃'
            else:
                emojy='😭'

            #Change color and label depending on prediction
            label_text=[]
            color=[]
            for label in labels:
                if label==1:
                    label_text.append('✅ Positive')
                    color.append('Green')
                else:
                    label_text.append('❌ Negative')
                    color.append('Red')

            #Write the main result
            f''' ## The level of happiness in **{location}** is {happiness}%  {emojy}'''

            col1, col2 = st.columns(2)

            # Column #1 with random tweets and their labels
            with col1:
                with st.expander(" See random Tweets"):
                    for twee , label, color in zip(tweet,label_text,color):
                        text=f'''{twee} is {label}'''.replace("\n","")
                        text_html = f'<p style="font-family:sans-serif; color:{color}; font-size: 20px; border-radius: 25px; border: 2px solid {color}; padding: 20px;">{text}</p>'
                        st.markdown(text_html, unsafe_allow_html=True)

            #Column #2 with charts
            with col2:

                #Line timeline chart
                y=res1['mean_day'].items()
                st.line_chart(pd.DataFrame(data=y,columns=['Day','Happiness']).set_index('Day'))

                # Pie chart
                emotions=np.array([happiness,100-happiness])
                my_labels=['Happy 😃','Sad 😭']
                colors=['#95CD41','#FA877F']
                fig, ax = plt.subplots()
                ax.pie(emotions,labels=my_labels,colors=colors)
                st.pyplot(fig)
