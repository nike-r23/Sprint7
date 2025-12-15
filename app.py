import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Título y texto
st.title("Mi Primera App con Streamlit")

nombre = st.text_input("¿Cómo te llamas?:") 
if st.button("Saludar"):
    st.write(f"¡Hola, {nombre}!.")
st.space(size="small")

st.header('Análisis de Datos de Venta de Vehículos')  
st.write('Esta aplicación analiza un conjunto de datos de anuncios de venta de vehículos en Estados Unidos')
st.space(size="small")         
st.write('Data Viewer') 
df = pd.read_csv('vehicles_us.csv') # leer los datos  
#Agregar una tabla
st.dataframe(df)
st.space(size="small")

st.title("Creación de Gráficos")
st.space(size='small')
st.write('Creación de un histograma de "Condicion" vs "Año del Modelo"')
hist_button = st.button('Construir histograma') # crear un botón
 
if hist_button: # al hacer clic en el botón
        
    # crear un histograma
    fig = px.histogram(df, x="model_year", color="condition" ,title="Condición de Vehiculos por Año del Modelo")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


st.space(size='small')
st.write('Creación de un Gráfico de Dispersión entre "Kilometraje" vs "Precio"')
dis_button = st.button('Construir gráfico de dispersión') # crear un botón
 
if dis_button: # al hacer clic en el botón
        
    # Gráfico de dispersión: Kilometraje vs Precio
    fig = px.scatter(df, x="odometer", y="price", color="type", title="Relación entre Kilometraje y Precio")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



st.space(size="small")
st.write('Creación de Gráfico para la Comparación de Precios entre 2 Modelos')
# Obtener los modelos de vehiculos 
top_models = df['model'].value_counts().index.tolist()

# Dos selectores simples
modelo1 = st.selectbox('Elige el primer modelo:', top_models)
modelo2 = st.selectbox('Elige el segundo modelo:', top_models)

# Botón para comparar
if st.button('Comparar modelos'):
    if modelo1 != modelo2:
        comparison_data = df[df['model'].isin([modelo1, modelo2])]
        fig = px.histogram(comparison_data, x="price", color="model",title=f"Comparación: {modelo1} vs {modelo2}")
        st.plotly_chart(fig)
    else:
        st.warning("Por favor selecciona dos modelos diferentes")