import  streamlit as st
import pandas as pd
st.set_page_config(page_title="Datos y Análisis",layout='wide')

def limpiar_datos():
    st.subheader("Limpieza de base de datos")
    file = st.file_uploader("Subir archivo CSV o excel",type=['csv','xlsx'])
    if file:
        if file.type == 'text/csv':
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
        st.dataframe(df)
        st.success("Dataframe cargado exitósamente")
        if st.button("Limpiar datos"):
            st.write("Empezando limpieza de datos...")

def main():
    st.header("Limpieza y resolución de datos")
    secciones = ['Limpieza de datos','Análisis de datos','Generador gráfico','Detección outliers']
    seccion = st.sidebar.selectbox("Sección",secciones)
    if seccion == 'Limpieza de datos':
        limpiar_datos()

if __name__ == '__main__':
    main()
