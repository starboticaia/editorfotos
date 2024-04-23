import streamlit as st
import numpy as np

logo = "http://starbotica.com/wp-content/uploads/2022/11/cropped-cropped-cropped-logo-fondo.jpg"
imagenLogo = Image.open(logo)

# Crear dos columnas con distinta anchura
col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Sube aquí tu foto...</p>', unsafe_allow_html=True)
    
with col2:
    st.image(imagenLogo,  width=150) 
