import pandas as pd
import plotly.express as px
import streamlit as st

df_car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# Agregamos una columna 'brand' para facilitar la manipulación de datos
df_car_data['brand'] = df_car_data.model.apply(lambda x: x.split()[0])

st.title('Proyecto del Sprint 6')

st.divider()

st.header('Visualizador de datos.')

####################################################################################
options = df_car_data.brand.unique().tolist()
selection = st.selectbox('Selecciona una marca', options, index=1)

df_cars_per_brand = df_car_data.query('brand == @selection')
df_cars_per_brand
####################################################################################
st.subheader('Estadisticas del precio de los autos')
metrics_button = st.button('Generar')  # crear un botón

if metrics_button:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Precio promedio",
                f"{round(df_cars_per_brand.price.mean(), 2)}$")
    col2.metric("Precio máximo", f"{df_cars_per_brand.price.max()}$")
    col3.metric("Precio mínimo", f"{df_cars_per_brand.price.min()}$")
    col4.metric("Autos listados", f"{df_cars_per_brand.price.count()}")
###########################################################################################

st.divider()

# escribir un mensaje
st.write(f'Distribución del precio de los autos para la marca {selection}')

# crear un histograma
fig = px.histogram(df_cars_per_brand, x="price")

# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True)
