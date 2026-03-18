#Importar librerias
import pandas as pd
import streamlit as st

def ordenar(df):
    st.subheader("Ordenación de datos")
    orden = st.selectbox("Columna a ordenar", df.columns)
    df_filtrado = df.sort_values(by=orden, ascending=False)
    st.dataframe(df_filtrado)
    nombre = st.text_input("Nombre del archivo", "datos_filtrados")
    csv = df_filtrado.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Descargar CSV",
        data=csv,
        file_name=f"{nombre}.csv",
        mime="text/csv"
    )

def filtrar(df):
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

def graficar(df):
    st.subheader("Graficar datos")
    import plotly.express as px
    graph = st.selectbox("Seleccionar tipo de gráfico", ['line', 'bar', 'scatter', 'hist', 'pie'])
    color = st.selectbox("Color (opcional)", [None] + list(df.columns))
    if graph == 'line':
        column1 = st.selectbox("Eje x", df.columns)
        column2 = st.selectbox("Eje y", df.columns)
        fig = px.line(df, column1, column2, color=color)
        st.plotly_chart(fig)
    elif graph == 'bar':
        column1 = st.selectbox("Eje x", df.columns)
        column2 = st.selectbox("Eje y", df.columns)
        fig = px.bar(df, column1, column2, color=color)
        st.plotly_chart(fig)
    elif graph == 'scatter':
        column1 = st.selectbox("Eje x", df.columns)
        column2 = st.selectbox("Eje y", df.columns)
        fig = px.scatter(df, column1, column2, color=color)
        st.plotly_chart(fig)
    elif graph == 'hist':
        column = st.selectbox("Columna", df.columns)
        fig = px.histogram(df, column, color=color)
        st.plotly_chart(fig)
    else:
        column = st.selectbox("Categoría", df.columns)
        fig = px.pie(df, names=column)
        st.plotly_chart(fig)

def main():
    st.title("Aplicación Análisis de Datos")
    st.write("La aplicación es ideal para mostrar resultados estadísticos y "
             "brindar información acerca de una base de datos ya sea con tablas"
             "excel o archivos csv. ")
    st.write("Ingresa tu dataset o datos para ser analizados y darte resultados"
             " reales")

    opcion = st.sidebar.selectbox('Menu',['Explorador dataframes','','App Machine learning'])
    if opcion == 'Explorador dataframes':
        st.subheader("Explorador de Dataframes ")
        file = st.file_uploader("Subir archivo",type=['csv','xlsx'])
        if file:
            st.success("Archivo subido con éxito")
            detalles = {'nombre': file.name,
                        'tipo': file.type,
                        'tamaño': file.size}
            st.write(detalles)
            if file.type == "text/csv":
                df = pd.read_csv(file)
            elif file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                df = pd.read_excel(file)
            st.dataframe(df)
            st.title("Análisis de datos")
            selec = st.selectbox("Método",['Ordenar','Filtrar','Graficar'])
            if selec == 'Ordenar': #Apartado de ordenar datos
                ordenar(df)
            elif selec == 'Filtrar': #Apartado de filtrar datos
                filtrar(df)
            elif selec == 'Graficar':
                graficar(df)

if __name__ == '__main__':
    main()