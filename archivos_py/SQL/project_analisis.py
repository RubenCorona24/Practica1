import streamlit as st
import pyodbc
import  numpy as np
import pandas as pd
import plotly.express as px
st.set_page_config(page_title='Análisis de Datos Spotify',page_icon="🎵")
st.title("Análisis Spotify Songs")

@st.cache_resource
#Función de conectar base de datos
def conectar_data():
    return pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=RubenSantiago;"
    "DATABASE=Pruebas SQL;"
    "Trusted_Connection=yes;")

#Función de obtener datos de la base de datos
@st.cache_data
def obtener_datos(query):
    conn = conectar_data()
    df = pd.read_sql(query, conn)
    return df
    #Devolvemos el dataframe
df_original = obtener_datos("SELECT * FROM SpotifySongs")
with st.sidebar:
    st.subheader("FILTROS")
    genero = st.multiselect("Géneros",df_original.primary_genre.unique())

    anios = sorted(df_original['release_year'].dropna().unique())
    year_range = st.slider(
        "Rango de años",
        min_value=int(min(anios)),
        max_value=int(max(anios)),
        value=(int(min(anios)), int(max(anios)))  # Rango completo por defecto
    )

df = df_original.copy()
if genero:
    df = df[df['primary_genre'].isin(genero)]
df = df[df['release_year'].between(year_range[0], year_range[1])]
st.subheader("Información acerca de las canciones más populares y artistas")

col1,col2,col3 = st.columns(3) #Creamos columnas
with col1:
    total_canciones = df.shape[0]
    st.metric("🎵Canciones totales ",total_canciones)
with col2:
    streams_promedio = np.round(np.mean(df['total_streams_billions']),2)
    st.metric("Billones de Streams Promedio",streams_promedio)
with col3:
    anio_max = df['release_year'].value_counts().idxmax() #Encuentra el mejor año
    st.metric("Año con más canciones",anio_max)
st.write("Dataset Spotify 2024")
st.dataframe(df)


#figura

if not df.empty:
    top10 = df.nlargest(10, 'total_streams_billions')  # Más robusto que head()
    fig = px.bar(
        top10,
        x='song_title',
        y='total_streams_billions',
        title='🏆 TOP 10 Canciones más exitosas',
        labels={'song_title': 'Canción', 'total_streams_billions': 'Streams (billions)'},
        color='total_streams_billions',
        color_continuous_scale='Greens'
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No hay datos con los filtros seleccionados.")

#Graficar canciones por año
cantidad_canciones = df.groupby('release_year').size().reset_index(name='cantidad')
fig2 = px.line(cantidad_canciones,x='release_year',y='cantidad',title='Canciones lanzadas por año',markers=True)
st.plotly_chart(fig2,use_container_width=True)

#Pie chart : Distribución por género
fig3  = px.pie(df,names=df.primary_genre,title='Distribución de Géneros Spotify')
st.plotly_chart(fig3)

#top artistas
top10_artistas = df.groupby('artist')['total_streams_billions'].sum().nlargest(10).reset_index()
fig4 = px.bar(top10_artistas,x='artist',y='total_streams_billions',title='TOP 10 Artistas')
st.plotly_chart(fig4)