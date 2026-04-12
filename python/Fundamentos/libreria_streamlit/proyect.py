import streamlit as st
import requests
import random
import pandas as pd

diccionario_personajes ={
    "goku": "1",
    "vegeta": "2",
    "piccolo": "3",
    "bulma": "4",
    "freezer": "5",
    "zarbon": "6"
}

def extraer_informacion(personaje):
    url = f"https://dragonball-api.com/api/characters/{diccionario_personajes[personaje]}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        return None


st.set_page_config(page_title="Información Dragon Ball",initial_sidebar_state="collapsed")
    


def personajes():
    if "lista_personajes" not in st.session_state:
        st.session_state.lista_personajes = []
    if "mostrar_df" not in st.session_state:
        st.session_state.mostrar_df = False

    st.subheader("Extrae información de tus personajes")
    personaje = st.text_input(label="Personaje")

    if personaje in diccionario_personajes:
        data = extraer_informacion(personaje)
        st.subheader("Información principal del personaje")
        st.write(f"Nombre del personaje: {data['name']}")
        st.write(f"Ki del personaje: {data['ki']}")
        st.write(f"Descripción del personaje: {data['description']}")
        st.write(f"Ki Máximo: {data['maxKi']}")
        st.write(f"Raza: {data['race']}")
        st.write(f"Género: {data['gender']}")

        if st.button("Guardar información del personaje"):
            st.session_state.lista_personajes.append({
                "Nombre": data['name'],
                "Ki": data['ki'],
                "Descripción": data['description'],
                "Ki Máximo": data['maxKi'],
                "Raza": data['race'],
                "Género": data['gender']
            })
            st.info(f"✅ {data['name']} guardado!")

    if st.button("Mostrar DataFrame de Personajes Guardados"):
        st.session_state.mostrar_df = True  # solo activa la bandera

    # Todo el DataFrame y filtros van AQUÍ, fuera de cualquier botón
    if st.session_state.mostrar_df:
        if st.session_state.lista_personajes:
            df = pd.DataFrame(st.session_state.lista_personajes)
            st.subheader("Personajes guardados")

            # --- Filtros ---
            col1, col2 = st.columns(2)

            with col1:
                orden = st.selectbox("Ordenar por columna", options=df.columns)
                ascendente = st.radio("Orden", ["Ascendente", "Descendente"]) == "Ascendente"

            with col2:
                filtro_raza = st.multiselect("Filtrar por Raza", options=df["Raza"].unique())
                filtro_genero = st.multiselect("Filtrar por Género", options=df["Género"].unique())

            # --- Aplicar filtros ---
            if filtro_raza:
                df = df[df["Raza"].isin(filtro_raza)]
            if filtro_genero:
                df = df[df["Género"].isin(filtro_genero)]

            df = df.sort_values(by=orden, ascending=ascendente)

            st.dataframe(df)

            # --- Estadísticas básicas ---
            if st.checkbox("Mostrar estadísticas del DataFrame"):
                st.write(df.describe(include="all"))

        else:
            st.warning("No hay personajes guardados aún.")
        nombre = st.text_input("Nombre del archivo", "datos_filtrados")
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
        label="Descargar CSV",
        data=csv,
        file_name=f"{nombre}.csv",
        mime="text/csv"
    )

def planetas():
    st.subheader("Extrae información de planetas")
    planeta = st.text_input(label="Planeta")

def main():
    st.title("API de Dragon Ball")
    secciones = ["Personajes","Planetas"]
    seccion = st.sidebar.selectbox("Menu",secciones)
    if seccion == "Personajes":
        personajes()
    else:
        planetas()
        

if __name__ == "__main__":
    main()
    

