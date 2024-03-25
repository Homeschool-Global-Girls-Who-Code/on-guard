import streamlit as st
from PIL import Image

st.set_page_config(
   page_title="About Us - On Guard",
)


col1, col2 = st.columns([0.25,1])
with col2:
   logo = Image.open("on_guard_logo.jpg")
   st.image(logo, width=400)

st.title('About Us')
st.subheader('On Guard is a parental control app created to assist parents and guardians to be a digital protector of their children in the online world.')
st.subheader('We aim to keep every Filipino child safe from the potential threats online and empower parents to their highest.')

st.subheader("Our Team")

#Jickle
Jickle = Image.open("Jickle_Clain_Ong.jpg")
st.image(Jickle, width=410)

#Luna
Luna = Image.open("Luna_Rinoa_Batungbakal.jpg")
st.image(Luna, width=480)


#Jameela
Jameela = Image.open("Jameela_Ysabella_Clay_Ong.jpg")
st.image(Jameela, width=500)

#Jana
Jana = Image.open("Jana_Annika_Uy.jpg")
st.image(Jana, width=540)

st.markdown("Representing Victory Christian International School - Homeschool Global")

