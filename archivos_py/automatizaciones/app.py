#Importamos librerías necesarias
import streamlit as st
import pandas as pd

#Cargamos nuestro dataframe
df = pd.read_csv('dataset_fifa_prueba.csv')

#Comenzamos con la creación de la aplicación en streamlit
def main():
    st.title('Página Inicial') #Crea un título tipo h1 de html
    st.text("Dentro de esta página encuentras información de los jugadores de la FIFA")
    st.header("Dataframe Jugadores de FIFA")
    st.dataframe(df) #Incorporamos el dataframe a la aplicación
    opcion = st.selectbox('Elige tu jugador favorito',['L.Messi','Cristiano Ronaldo','Neymar','Mbappé']) #Caja de selección
    st.write(f"Jugador Favorito: {opcion}")
    nombre = st.text_input('Ingresa tu nombre')
    edad = st.slider('Ingresa tu edad',0,100,value=25) #Insertamos slider
    st.write(f"Edad: {edad}")
    fecha = st.date_input('Selecciona la fecha')
    st.time_input("Selecciona la hora")
    st.write(f"Muchas gracias usuario, se guardó tu registro con la siguiente informacion: Nombre-{nombre} Edad-{edad} Jugador Fav-{opcion} Fecha-{fecha}")
if __name__ == '__main__':
    main()