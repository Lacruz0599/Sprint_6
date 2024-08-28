import pandas as pd
import plotly.express as px
import streamlit as st

df_car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# Agregamos una columna 'brand' para facilitar la manipulación de datos
df_car_data['brand'] = df_car_data.model.apply(lambda x: x.split()[0])

st.title('Proyecto del Sprint 6')  # Configuramos el titulo de la página

st.divider()

############################ --Visualizador de datos--########################################################
st.header('Visualizador de datos.')
# Obtenemos una lista con todas las marcas de vehiculos
options = df_car_data.brand.unique().tolist()
# Configuramos el cuadro de selección
selection = st.selectbox('Selecciona una marca', options, index=1)
# Filtramos los autos según la seleccion del usuario
df_cars_per_brand = df_car_data.query('brand == @selection')
df_cars_per_brand  # Se imprime en pantalla el dataframe resultante

################################# --Estadisticas--###################################################

st.subheader(f'Estadisticas del precio de los autos {selection}')
# crear un botón para calcular las estadisticas básicas
metrics_button = st.button('Generar')

if metrics_button:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Precio promedio",
                f"{round(df_cars_per_brand.price.mean(), 2)}$")  # Calcula el precio promedio para los autos de es marca
    # Calcula el precio máximo para los autos de es marca
    col2.metric("Precio máximo", f"{df_cars_per_brand.price.max()}$")
    # Calcula el precio mínimo para los autos de es marca
    col3.metric("Precio mínimo", f"{df_cars_per_brand.price.min()}$")
    # Calcula el precio promedio para los autos de es marca
    col4.metric("Autos listados", f"{df_cars_per_brand.price.count()}")


################################# --Histograma--##########################################################

st.divider()
# escribir un mensaje
st.subheader(f'Distribución del precio de los autos para la marca {selection}')
# crear un histograma
fig = px.histogram(
    df_cars_per_brand,
    x="price",
    color_discrete_sequence=['#EF553B'])
# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True)

################################# --Gráfico de dispersión--##########################################################
# escribir un mensaje
st.subheader(f'Relación entre el precio y el odometro {selection}')
# crear un gráfico de dispersión
fig = px.scatter(
    df_cars_per_brand,
    x="odometer",
    y="price",
    color_discrete_sequence=['#EF553B'])

st.plotly_chart(fig, use_container_width=True)
