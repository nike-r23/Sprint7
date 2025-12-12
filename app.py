import streamlit as st

# Title
st.title("Mi primera app")

# Sidebar
st.sidebar.header("Settings")
name = st.sidebar.text_input("Ingresa tu nombre")
# Conditional greeting
if name:
    st.info(f"Hola, {name}! Gracias.")