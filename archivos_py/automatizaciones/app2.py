import streamlit as st
import plotly.express as px
import pandas as pd

#Importamos nuestro dataframe
df = pd.read_csv('coffee_sales.csv')

#Configuramos nuestro entorno de streamlit
st.set_page_config(page_title='MI APP',layout='wide',initial_sidebar_state='collapsed')

#Creamos nuestra aplicación con main
def main():
    st.title("Datos de Venta Cafetería")
    st.sidebar.header('Navegación')
    st.dataframe(df) #Dataframe en pantalla
    conteo = df['cash_type'].value_counts()
    st.write(conteo)
    df_agrupado = df.groupby('cash_type').count().reset_index()
    #creamos figura
    fig = px.pie(df_agrupado,names='cash_type',values='money',title='Tipo de pago y dinero')
    #INsertamos la gráfica en la aplicación
    st.plotly_chart(fig)
    st.write(df['coffee_name'].value_counts())
    #Creamos nueva figura de barras
    fig2 = px.bar(df,'coffee_name','money',title='Precios de productos')
    st.plotly_chart(fig2)

if __name__ == '__main__':
    main()


