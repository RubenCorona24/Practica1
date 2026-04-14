import streamlit as st
import requests
import random

def obtener_datos_personaje(personaje):
    url = f"https://dragonball-api.com/api/characters/{personaje}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        data = respuesta.json()
        return data
    else:
        return None

def info_personaje(data):
    nombre = data['name']
    ki = data['ki']
    descripcion = data['description']
    return nombre,ki,descripcion

def informacion():
    st.subheader("Extrae información de personajes de DB")
    st.write("Escribe el nombre del personaje deseado")
    seleccion = st.text_input(label="Personaje").lower()
    if st.button("Extraer información"):
        if seleccion == "goku":
            data = obtener_datos_personaje("1")
            nombre,ki,descripcion = info_personaje(data)
            st.subheader(f"Selección: {data[nombre]}")


st.set_page_config(page_title="Información Dragon Ball",initial_sidebar_state="collapsed")
def main():
    secciones = ['Principal','Información']
    opcion = st.sidebar.selectbox("Menu",secciones)
    if opcion == "Principal":
        st.title("API de Dragon Ball")
        st.write("""Dentro de esta aplicación podrás encontrar información importante acerca de tus personajes favoritos de Dragon Ball
                    , en la parte de Información podrás acceder a información específica de cada uno de ellos""")
    else:
        informacion()

if __name__ == "__main__":
    main()

