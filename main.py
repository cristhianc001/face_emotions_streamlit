import streamlit as st

@st.cache_resource
def load_portrait():
    return st.image('https://raw.githubusercontent.com/cristhianc001/Analisis-Sentimientos-Hoteles/main/img/1.jpg')
load_portrait()