import streamlit as st
import seaborn as sns
import yfinance as yf #precios de las acciones en tiempo real 
import plotly.express as px

df =  sns.load_dataset("titanic")

st.title("Mi primera app Web")
st.space(size="medium")
st.write("Escribiendo texto")
st.space(size="small")
nombre = st.text_input("Ingrese su Nombre:")
st.space(size="small")
if nombre:
    st.write(f"Hola: {nombre}")
#Agregar una tabla
st.dataframe(df)
#yahoo finance
st.space(size="medium")
nombre_del_activo = st.text_input("Ingresa el symbol (e.g., NVDA, BTC-USD)", "NVDA")
stock = yf.Ticker(nombre_del_activo)
df_stocks = stock.history(period="1y")
fig = px.line(df_stocks)
st.plotly_chart(fig)


