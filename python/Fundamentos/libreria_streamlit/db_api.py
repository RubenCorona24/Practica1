import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import re

st.set_page_config(page_title="Información Dragon Ball",initial_sidebar_state="collapsed")
def obtener_datos(id):
    url = f"https://dragonball-api.com/api/characters/{id}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        nombre = data['name']
        ki = data['ki']
        maxKi = data['maxKi']
        descripcin = data['description']
        raza = data['race']
        genero = data['gender']
        return nombre,ki,maxKi,descripcin,raza,genero
    else:
        return None

@st.cache_data
def dataframe():
    lista = []  # acumulas aquí todos los personajes
    
    for n in range(1, 59):
        resultado = obtener_datos(n)
        if resultado is not None:  # por si alguna petición falla
            nombre, ki, maxKi, descripcion, raza, genero = resultado
            lista.append({
                'Nombre': nombre,
                'Ki': ki,
                'Ki Máximo': maxKi,
                'Descripción': descripcion,
                'Raza': raza,
                'Género': genero
            })

    # El DataFrame se crea UNA sola vez con toda la lista
    df = pd.DataFrame(lista)
    return df

def convertir_ki(valor):
    if not valor or valor.strip() == "0":
        return 0
    
    valor = valor.strip().replace(",", ".")
    
    # Detectar palabras grandes
    multipliers = {
        "billion":    1_000_000_000,
        "trillion":   1_000_000_000_000,
        "quadrillion":1_000_000_000_000_000,
        "quintillion":1_000_000_000_000_000_000,
        "sextillion": 1_000_000_000_000_000_000_000,
        "septillion": 1_000_000_000_000_000_000_000_000,
    }
    
    valor_lower = valor.lower()
    for palabra, mult in multipliers.items():
        if palabra in valor_lower:
            numero = re.findall(r"[\d.]+", valor_lower)
            if numero:
                return float(numero[0]) * mult
    
    # Si es número con puntos como separador de miles (60.000.000)
    try:
        return float(valor.replace(".", ""))
    except:
        return 0
    
df = dataframe()
# Limpiar el DataFrame
df["Ki_num"]    = df["Ki"].apply(convertir_ki)
df["MaxKi_num"] = df["Ki Máximo"].apply(convertir_ki)

def info_planetas(id):
    url = f"https://dragonball-api.com/api/planets/{id}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        nombre = data['name']
        isDestroyed = data['isDestroyed']
        descripcion = data['description']
        return nombre,isDestroyed,descripcion
    else:
        return None
    
@st.cache_data
def dataframe_planetas():
    lista_planetas = []
    for n in range(1,21):
        resultado= info_planetas(n)
        if resultado is not None:
            nombre,isDestroyed,descripcion = resultado
            lista_planetas.append({
                "Nombre":nombre,
                "Destruido":isDestroyed,
                "Descripción":descripcion
            })
    df_planetas = pd.DataFrame(lista_planetas)
    return df_planetas

df_planetas = dataframe_planetas()

def graficar(df):
    df_ordenado = df.sort_values(by='Ki_num',ascending=False)
    fig = px.bar(df_ordenado.head(10),'Nombre','Ki_num',title="Personajes más poderosos")
    return fig


def filtros(df):
    st.subheader("Filtros")
    st.write("Añade filtros al Dataframe")
    modo = st.selectbox("Modo",['Ordenar','Agrupar','Filtrar'])
    if modo is not None:
        if modo == "Ordenar":
            orden = st.selectbox("Columna a ordenar",df.columns)
            df_ordenado = df.sort_values(by=orden,ascending=False)
            st.dataframe(df_ordenado)
            nombre = st.text_input("Nombre del archivo", "datos_filtrados")
            csv = df_ordenado.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Descargar CSV",
                data=csv,
                file_name=f"{nombre}.csv",
                mime="text/csv"
            )
        elif modo=="Agrupar":
            grupo = st.selectbox("Columna por agrupar",df.columns)
            agregacion = st.selectbox("Agregación", ["count", "mean", "sum"])
            df_agrupado = df.groupby(grupo)[["Ki_num", "MaxKi_num"]].agg(agregacion).reset_index()
            st.dataframe(df_agrupado)
            nombre = st.text_input("Nombre del archivo", "datos_filtrados")
            csv = df_agrupado.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Descargar CSV",
                data=csv,
                file_name=f"{nombre}.csv",
                mime="text/csv"
            )
        else:
            st.subheader("Filtración de datos")
            filtro = st.selectbox("Filtrar por", df.columns)
            # Detectar tipos de datos
            if df[filtro].dtype == 'object':
                valores = st.multiselect("Selecciona valores", df[filtro].unique())
                df_filtrado = df[df[filtro].isin(valores)]
            else:
                min_val = float(df[filtro].min())  # Definimos el valor mínimo
                max_val = float(df[filtro].max())  # Definimos el valor máximo
                rango = st.slider("Selecciona rango", min_val, max_val,
                                (min_val, max_val))  # Creamos slider con valor mínimo y máximo
                df_filtrado = df[
                    (df[filtro] >= rango[0]) &
                    (df[filtro] <= rango[1])]  # Filtramos el dataframe
            st.dataframe(df_filtrado)  # Mostramos el dataframe filtrado
            nombre = st.text_input("Nombre del archivo", "datos_filtrados")
            csv = df_filtrado.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Descargar CSV",
                data=csv,
                file_name=f"{nombre}.csv",
                mime="text/csv"
            )
def graficos(df):
    st.subheader("Gráficos")
    st.write("Generar gráficos")
    tipo = st.selectbox("Tipo",['Barra','Líneas','Dispersión','Histograma'])
    if tipo is not None:
        if tipo == "Barra":
            column1 = st.selectbox("Columna 1",df.columns)
            column2 = st.selectbox("Columna 2",df.columns)
            title = st.text_input("Título del Gráfico"," ")
            fig = px.bar(df,column1,column2,title=title)
            st.plotly_chart(fig)
        elif tipo == "Líneas":
            column1 = st.selectbox("Columna 1",df.columns)
            column2 = st.selectbox("Columna 2",df.columns)
            title = st.text_input("Título del Gráfico"," ")
            fig = px.line(df,column1,column2,title=title)
            st.plotly_chart(fig)
        elif tipo == "Dispersión":
            column1 = st.selectbox("Columna 1",df.columns)
            column2 = st.selectbox("Columna 2",df.columns)
            title = st.text_input("Título del Gráfico"," ")
            fig = px.scatter(df,column1,column2,title=title)
            st.plotly_chart(fig)
        else:
            column = st.selectbox("Columna",df.columns)
            title = st.text_input("Título del Gráfico", " ")
            fig = px.histogram(df,column,title=title)
            st.plotly_chart(fig)


            

def main():
    st.title("Información de Dragon Ball")
    seccion = st.sidebar.selectbox("Sección",['Personajes','Planetas'])
    if seccion == "Personajes": #Sección de personajes
        st.subheader("Información Acerca de Personajes")
        st.write("En la API, hay 58 personajes")
        st.dataframe(df)
        if "mostrar_grafica" not in st.session_state:
            st.session_state.mostrar_grafica = False

        if st.button("Gráficas"):
            st.session_state.mostrar_grafica = True

        if st.session_state.mostrar_grafica:
            fig = graficar(df)
            st.plotly_chart(fig)
        filtros(df)
        graficos(df)
        
    else:
        st.subheader("Información Acerca de Planetas")
        st.write("En API de DB hay 10 planetas")
        st.dataframe(df_planetas)
        filtros(df_planetas)
        graficos(df_planetas)


if __name__ == "__main__":
    main()
