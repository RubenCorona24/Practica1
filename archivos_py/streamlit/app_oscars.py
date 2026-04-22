#Creamos app de streamlit oscars
import pandas as pd
import streamlit as st
import numpy as np
import pyodbc
import plotly.express as px
from queries import datos

#Accedemos a la base de datos
df,top_compositores,premios_anio,compositor_exitoso = datos()

#Configuramos nuestra app
st.set_page_config(page_title="Dashboard Premios Oscars",initial_sidebar_state="collapsed")

# --- Sidebar (FUERA de main) ---
st.sidebar.title("Filtros")
compositores_lista = ['Todos'] + sorted(df['Composer'].unique().tolist())
compositor_sel = st.sidebar.selectbox("Compositor", compositores_lista)

# --- Filtro aplicado (FUERA de main) ---
if compositor_sel != 'Todos':
    df_filtrado = df[df['Composer'] == compositor_sel]
else:
    df_filtrado = df

#Filtro de fecjha
fecha_min,fecha_max = int(df['Year'].min()),int(df['Year'].max()) #Años minimo y máximo
filtro = st.slider("Filtro de año",fecha_min,fecha_max,(fecha_min, fecha_max))
df_filtrado = df[(df["Year"]>=filtro[0]) & (df["Year"] <=filtro[1])]

    
#Creamos figuras con plotly
fig1 = px.bar(top_compositores,'Composer','Premios',title="Mejores Compositores",color='Premios',color_continuous_scale="Blues")
fig2 = px.line(premios_anio,"Year",'Premios',title="Premios por año",markers=True)
fig3 = px.histogram(df.assign(Decada=(df_filtrado['Year']//10)*10),
                    x='Decada',title="Premios por década",color_discrete_sequence=['steelblue'])
fig4 = px.scatter(df_filtrado,x='Year',y='Composer',hover_data=['Film'],title="Linea de tiempo de ganadores")
fig4.update_layout(showlegend=False)

def main():
    st.title("Dashboard dePremios Oscars de Películas🎬")
    col1,col2,col3 = st.columns(3)
    col1.metric("Total de Premios Oscars",len(df_filtrado) )
    col2.metric("Cantidad de compositores",len(df_filtrado['Composer'].value_counts()))
    col3.metric("Compositor más exitoso 🔥",compositor_exitoso['Composer'][0])
    st.subheader("Información general de Películas")
    st.dataframe(df_filtrado)
    st.subheader("Dashboards")
    st.plotly_chart(fig1)
    col_a,col_b = st.columns(2)
    col_a.plotly_chart(fig2,use_container_width=True)
    col_b.plotly_chart(fig3,use_container_width=True)
    st.plotly_chart(fig4,use_container_width=True)    
    st.subheader("Buscador de Películas")
    busqueda = st.text_input("Escribe el nombre de la película")
    if busqueda:
        r = df[df['Film'] == busqueda]
        if not r.empty:
            st.dataframe(r)
        else:
            st.warning("No se encontró la película")


if __name__ == "__main__":
    main()