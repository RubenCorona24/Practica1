import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import re

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

def graficar(df):
    df_ordenado = df.sort_values(by='Ki_num',ascending=False)
    fig = px.bar(df_ordenado.head(10),'Nombre','Ki_num',title="Personajes más poderosos")
    return fig

st.set_page_config(page_title="Información Dragon Ball")

def main():
    st.title("Información de Dragon Ball")
    seccion = st.sidebar.selectbox("Sección",['Personajes','Planetas'])
    if seccion == "Personajes": #Sección de personajes
        st.subheader("Información Acerca de Personajes")
        st.write("En la API, hay 58 personajes")
        st.dataframe(df)
        if st.button("Graficas"): #Boton de graficar
            fig = graficar(df)
            st.plotly_chart(fig) #Mostramos la figura
    else:
        st.subheader("Información Acerca de Planetas")
        st.write("En API de DB hay 10 planetas")

if __name__ == "__main__":
    main()
