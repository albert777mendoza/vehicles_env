import streamlit as st
import pandas as pd
import plotly.express as px

# leer el dataset
df = pd.read_csv('vehicles_us.csv')

# encabezado de la aplicación
st.header('Análisis exploratorio de Datos de Vehículos')

# Botón para construir un Histograma
if st.button('Construir Histograma'):
    st.write("Histograma de la columna 'price'")
    if 'price' in df.columns:
        fig = px.histogram(df, x='price', title='Histograma de Precio')
    else: 
        # Si no existe 'price', usa la primera columna disponible
        first_col = df.columns[0]
        fig = px.histogram(df, x=first_col, title=f'Histograma de {first_col}')
    
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir un gráfico de dispersión
if st.button('Construir Scatter Plot'):
    st.write("Gráfico de Dispersión: Precio vs model_year")
    
    if 'price' in df.columns and 'model_year' in df.columns: 
        fig2 = px.scatter(df, x='price', y='model_year', title='Precio vs Año del Modelo')
        st.plotly_chart(fig2, use_container_width=True)
    else: 
        st.write("Las columnas necesarias para el scatter plot no están disponibles.")       
                        