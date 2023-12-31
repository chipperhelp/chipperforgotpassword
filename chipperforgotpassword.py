import streamlit as st
import pyrebase
from datetime import datetime
from streamlit_option_menu import option_menu
from PIL import Image
import requests
import streamlit.components.v1 as components
import random
import json
from io import BytesIO
import feedparser
import urllib.request
from datetime import datetime,timedelta
import uuid
import ast 

#streamlit=1.24.0
#on streamlit cloud streamlit=1.16.0
#current version changed to streamlit=1.16.0 from streamlit=1.24.0











logot=Image.open("logo.png")

st.set_page_config(page_title="Chipper",page_icon=logot,layout='wide',initial_sidebar_state='auto')





hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            #GithubIcon{visiblity:hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)





button_style = '''
    <style>
        .stButton button {
            background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
            color: #FFFFFF; 
            border-color:#2DB4EC; 
        }
    </style>
'''


st.markdown(button_style, unsafe_allow_html=True)
st.markdown('<style>.stButton>button { margin-left: auto; margin-right: auto; display: block; }</style>', unsafe_allow_html=True)




textcolor= """
    <style>
    .textlogin{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-style:italic;color:#1A6DFF;text-align:left;font-size:30px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)


textcolor= """
    <style>
    .text{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-style:italic;color:#1A6DFF;text-align:center;font-size:30px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)





firebaseConfig = {
  "apiKey": "AIzaSyDQkowU9ElUDooKZKb-b-g6beWBF30glv0",
  "authDomain": "chipper1-2980f.firebaseapp.com",
  "databaseURL": "https://chipper1-2980f-default-rtdb.firebaseio.com",
  "projectId": "chipper1-2980f",
  "storageBucket": "chipper1-2980f.appspot.com",
  "messagingSenderId": "276274547796",
  "appId": "1:276274547796:web:9593e0f6fdd3afba8471c1",
  "measurementId": "G-2NPS52N6ZX"
}
firebase= pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

data=firebase.database()
storage=firebase.storage()


textcolor= """
    <style>
    .holdertext{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-style:italic;color:#1A6DFF;text-align:left;font-size:30px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)
       

textcolor= """
    <style>
    .holdertexts{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-style:italic;color:#1A6DFF;text-align:center;font-size:25px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)

streamlitstyle = """
			<style>
			sidebar,body,[class*="css"]{background-image: url("https://cdn.theatlantic.com/thumbor/Sy0CJqDYC9tkLmlM1XA4GgksyYo=/0x0:3500x1969/960x540/media/img/mt/2023/02/yo_yo_economy/original.gif");
                        background-attachment: fixed;
                        background-size: cover 
			
			
                       
			
			
                        }
			</style>
			"""



#st.markdown(streamlitstyle, unsafe_allow_html=True)

font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 20px;
  padding:10px
}
</style>
"""
st.write(font_css, unsafe_allow_html=True)

st.markdown("<center><img src=https://img.icons8.com/fluency/500/soulseek.png; alt=centered image; height=150; width=150> </center>",unsafe_allow_html=True)
textcolor= """
    <style>
    .gradient-text{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-weight: 600;font-style:italic;color:#1A6DFF;text-align:center;font-size:30px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)
st.markdown('<p class="gradient-text">ℂ𝕙𝕚𝕡𝕡𝕖𝕣</p>', unsafe_allow_html=True)



textcolor= """
    <style>
    .gradienttext{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-weight: 600;font-style:italic;color:#1A6DFF;text-align:left;font-size:30px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)
# st.markdown("<p class='holdertext'>Login or Register :</p>", unsafe_allow_html=True)


textcolor= """
    <style>
    .gradienttextt{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-weight: 600;font-style:italic;color:#1A6DFF;text-align:left;font-size:15px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)
button_style = '''
    <style>
        .stButton button {
            background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
            color: #FFFFFF; 
            border-color:#2DB4EC; 
        }
    </style>
'''


st.markdown(button_style, unsafe_allow_html=True)
st.markdown('<style>.stButton>button { margin-left: auto; margin-right: auto; display: block; }</style>', unsafe_allow_html=True)

with st.form("resetpassword"):
    st.markdown('<p class="gradienttext">Forgot password?</p>', unsafe_allow_html=True)
    st.markdown('<p class="gradienttextt">Reset password in few steps</p>', unsafe_allow_html=True)
    email=st.text_input("",placeholder="Email")
    subbt=st.form_submit_button("Reset password")
    if subbt:
        if not email :
            st.toast("⚠️ Please enter your email address !")
        else:
            try:
                auth.send_password_reset_email(email)
                st.success("Reset password link has been successfully sent to  "+email)
            except:
                st.toast("🚫 Invalid email address")
#st.markdown(f"___")



         
st.write('<div style="text-align: center;"><a href="https://chipper.streamlit.app">Return back to Log in page</a></div>', unsafe_allow_html=True)
#http://localhost:8501/

