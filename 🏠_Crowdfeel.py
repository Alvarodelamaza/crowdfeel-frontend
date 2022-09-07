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
     page_icon="favicon2.png",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://github.com/Alvarodelamaza/crowdfeel',
         'Report a bug': "https://github.com/Alvarodelamaza/crowdfeel",
         'About': "## Population sentiment analysis using tweets \n Bootcamp project developed by: \n Alvaro de la Maza, Angelo Darriet, Beauregard Sangkala and Tjebbe Lodeizen"
     }
 )

# Title and subtitle
#title='👥 Crowdfeel 👥'
st.image('Logo3.png')

c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')

subtitle="The tool to track people's sentiment 💬"
#st.markdown(f"<h1 style='text-align: center;font-size: 60px;'>{title}</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center;font-size: 35px; color:#0B0500;'>{subtitle}</h1>", unsafe_allow_html=True)
subtitle2="About the tool 🔧 "
c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')
c=st.empty()

st.markdown(f"<h1 style='text-align: center;font-size: 45px;'>{subtitle2}</h1>", unsafe_allow_html=True)

subtitle4="CrowdFeel extract sentiments and emotions from the tweets from the last 7 days. With help of a Deep Learning model trained in more than 1.6M tweets, we are able to predict the mood of the user behinfd the tweet."

st.markdown(f"<h1 style='text-align: center;font-size: 28px;'>{subtitle4}</h1>", unsafe_allow_html=True)

c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')



subtitle3="About us 👥 "

st.markdown(f"<h1 style='text-align: center;font-size: 45px;'>{subtitle3}</h1>", unsafe_allow_html=True)
c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('👷‍♂️' 'Alvaro de la Maza, Chief Technology Officer')
    st.image('alvaro.png')
with col2:
    st.markdown('👨‍🚒' 'Angelo Darriet, Chief Operational Officer')
    st.image('angelo.png')
with col3:
    st.markdown('👨‍🏭' 'Beauregard Sangkala, Chief Marketing Officer')
    st.image('beau.png')

with col4:
    st.markdown('🕵️‍♂️' 'Tjebbe Lodeizen, Chief Financial Officer')
    st.image('tjebbe.png')



c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')
col5, col6, col7, df,rfr = st.columns(5)
with col7:
   st.image('lewagon.png',width=130)
