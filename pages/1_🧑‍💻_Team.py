
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
     page_title="Team CrowdFeel",
     page_icon="👥",
     layout="wide",
    initial_sidebar_state="collapsed",
     menu_items={
         'Get Help': 'https://github.com/Alvarodelamaza/crowdfeel',
         'Report a bug': "https://github.com/Alvarodelamaza/crowdfeel",
         'About': "## Population sentiment analysis using tweets \n Bootcamp project developed by: \n Alvaro de la Maza, Angelo Darriet, Beauregard Sangkala and Tjebbe Lodeizen"
     }
 )
st.image('banner.png')

# Title and subtitle
title='👥 Meet the team 👥'
subtitle="The people that have created the tool 💬"
st.markdown(f"<h1 style='text-align: center;font-size: 60px;'>{title}</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center;font-size: 35px;'>{subtitle}</h1>", unsafe_allow_html=True)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('👷‍♂️' 'Alvaro de la Maza, Chief Technology Officer')
    st.image('alvaro.png')
with col2:
    st.markdown('👨‍🚒' 'Angelo Darriet, Chief Operational Officer')
    st.image('angelo.png')
with col3:
    st.markdown('👨‍🏭' 'Beau Sangkala, Chief Marketing Officer')
    st.image('beau.png')

with col4:
    st.markdown('🕵️‍♂️' 'Tjebbe Lodeizen, Chief Financial Officer')
    st.image('tjebbe.png')


col5, col6, col7 = st.columns(3)

with col6:
   st.image('lewagon.png')
