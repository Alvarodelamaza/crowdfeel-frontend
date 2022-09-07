from pickletools import read_bytes1
import streamlit as st

import requests
import pandas as pd
import numpy as np
import seaborn as sns
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

#Palette picture
st.image('banner.png')


#Blank space
c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')


# Title and subtitle
title='Search by #hashtag '
subtitle="The tool to extract sentiments from a hashtag 💬"
subtitle_1="Extract sentiments...    ✅ vs. ❌"
subtitle_2="Extract emotions like: "
subtitle_3="😃 Happiness, 🤬 Hate, 😍 Love, 😐 Neutrality, 😭 Sadness, 😲 Surprise or 😱 Worry "
st.markdown(f"<h1 style='text-align: center;font-size: 60px;color :#0B0500;'>{title}</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center;font-size: 35px;color: #0B0500';>{subtitle}</h1>", unsafe_allow_html=True)

c=st.empty()
c.write(' ')
# Search form hashtag
st.markdown(f"<h1 style='text-align: center;font-size: 35px;color: #0B0500';>{subtitle_1}</h1>", unsafe_allow_html=True)
with st.form("search_form_sentiments_hashtag"):

    # Date filter
    #st.markdown(f"<h1 style='text-align: center;font-size: 30px;'>When? 📆</h1>", unsafe_allow_html=True)
    #col1, col2 = st.columns(2)
    #date_start = col1.date_input(' From...', value=datetime.datetime(2022, 8, 1, 12, 10, 20))
    #date_finish = col2.date_input(' ...to', value=datetime.datetime(2022, 8, 31, 12, 10, 20))

    # Hashtag filter
    st.markdown(f"<h1 style='text-align: center;font-size: 30px;'>What? #️⃣</h1>", unsafe_allow_html=True)
    col1,col3, col4 = st.columns(3)
    hashtag=col3.text_input(''' Hashtag you want to search ''')

    col11, col21 , col23,col34, col31 = st.columns(5)

    # Submit button
    col11, col21 , col23,col34, col31 = st.columns(5)
    submitted = col23.form_submit_button("Extract Sentiments from hashtag #️⃣ ")
    if submitted:

            # Print search filters
            st.write("Hashtag searched:  ", hashtag)

            # Call our API
            url=f'https://crowfeel-img-h5bk6vemiq-ez.a.run.app/predicthas?hashtag={hashtag}'
            #Loading... spinner
            with st.spinner('Extracting sentimentss.. 😃😭🤬😳'):
                res=requests.get(url).json()
                happiness=np.round(res['happiness'],2)
                tweet=res['tweet']
                labels=res['label']
            st.success('Sentiments extracted succesfully!',icon='✅')

            # Set the emojis
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
            f''' ## The happiness for #**{hashtag}** is {happiness}%  {emojy}'''

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
                # if timeline:
                #     y=res['mean_day'].items()
                #     st.line_chart(pd.DataFrame(data=y,columns=['Day','Happiness']).set_index('Day'))

                # Pie chart
                emotions=np.array([happiness,100-happiness])
                my_labels=['Happy 😃','Sad 😭']
                colors=['#AAF683','#F74052']
                plt.figure(figsize=(2, 2))
                fig, ax = plt.subplots()
                ax.pie(emotions,labels=my_labels,colors=colors)
                st.pyplot(fig)

st.markdown(f"<h1 style='text-align: center;font-size: 35px;color: #0B0500';>{subtitle_2}</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center;font-size: 35px;color: #0B0500';>{subtitle_3}</h1>", unsafe_allow_html=True)
with st.form("search_form_emotions_hashtag"):
    st.markdown(f"<h1 style='text-align: center;font-size: 30px;'>What? #️⃣</h1>", unsafe_allow_html=True)
    col1 , col3, col4 = st.columns(3)
    hashtag=col3.text_input(''' Hashtag you want to search ''')

    # Submit button
    col11, col21 , col23,col34, col31 = st.columns(5)
    submitted = col23.form_submit_button("Extract emotions from hashtag #️⃣ ")
    if submitted:

            # Print search filters
            st.write("Hashtag searched:  ", hashtag)

            # Call our API
            url=f'https://crowfeel-img-h5bk6vemiq-ez.a.run.app/predictemotionshas?hashtag={hashtag}'
            #Loading... spinner
            with st.spinner('Extracting emotions... 😃😭🤬😳'):
                res=requests.get(url).json()
                print(res)
                emotions_totaldf=pd.DataFrame(np.array(res['emotions']))
                tweet=res['tweet']
                emotionsdf=pd.DataFrame(np.array(res['label']))
            st.success('Emotions extracted succesfully!',icon='✅')

            emotions=np.array(emotionsdf[0].map({0.0:'Happiness 😃',1.0:'Hate 🤬',2.0:'Love 😍',3.0:'Neutral 😐',4.0:'Sadness 😭',5.0:'Surprise 😲',6.0:'Worry 😱'}))
            emotions_total=np.array(emotions_totaldf[0].map({0.0:'Happiness',1.0:'Hate',2.0:'Love',3.0:'Neutral',4.0:'Sadness',5.0:'Surprise',6.0:'Worry'}))

            col1, col2 = st.columns(2)

            # Column #1 with random tweets and their labels

            with st.expander(" See random Tweets"):
                for twee, emotion in zip(tweet,emotions):
                    text=f'''{twee} implies {emotion}'''.replace("\n","")
                    text_html = f'<p style="font-family:sans-serif; font-size: 20px; border-radius: 25px; border: 2px solid; padding: 20px;">{text}</p>'
                    st.markdown(text_html, unsafe_allow_html=True)

            #Column #2 with charts

            sentence_dictionary = {}
            word_counts = 0
            for item in emotions_total:
                if item in sentence_dictionary:
                    sentence_dictionary[item][0] += 1
                else:
                    sentence_dictionary[item] = [1]
            print(sentence_dictionary)
            word_df=pd.DataFrame(sentence_dictionary)
            # Bar chart
            sns.set(font_scale=1.3)
            colors={'Happiness':'#AAF683','Hate':'#F74052' ,'Love':'#FF7738','Neutral':'#FFD952','Sadness':'#51CBDB','Surprise':'#8312ED','Worry':'#9FFFCB'}
            fig = plt.figure(figsize=(10, 4))
            sns.barplot(x=word_df.columns,y=word_df.values[0],palette=colors)
            st.pyplot(fig)

c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')
c=st.empty()
c.write(' ')

st.image('palette_header.png')
