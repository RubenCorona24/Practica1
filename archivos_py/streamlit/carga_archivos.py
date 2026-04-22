#Importamos librerías
import streamlit as st
import pandas as pd
from PIL import  Image
import docx2txt
from PyPDF2 import  PdfReader

#Creamos función de cargar imagen
@st.cache_data
def cargar_imagen(img_file):
    img = Image.open(img_file)
    return img #Nos devuelve la imagen

#Función de leer pdf
def leer_pdf(file):
    pdfReader = PdfReader(file)
    paginas = len(pdfReader.pages)
    texto = ""
    for n in range(paginas):
        pagina = pdfReader.pages[n]
        texto+=pagina.extractText() #Escribimos la información en la página
    return texto #Nos devuelve el texto

#Creamos la aplicación
def main():
    st.title("Aplicación carga de archivos")
    opciones = ['Imágenes','Conjuntos de datos','Documentos']
    eleccion = st.sidebar.selectbox('Menú',opciones) #Creamos el selectbox con siderbar
    #Empezamos a trabajar con las opciones
    if eleccion=='Imágenes':
        st.subheader('Imágenes')
        archivo_imagen = st.file_uploader('Subir imagen',type=['png','jpg','jpeg'])
        if archivo_imagen is not None:
            detalles_imagen = {"nombre": archivo_imagen.name,
                               "tipo": archivo_imagen.type,
                               'tamaño': archivo_imagen.size}
            st.write(detalles_imagen) #Escribimos el detalle de la imagen
            #Insertamos la imagen
            st.image(cargar_imagen(archivo_imagen),width=250) #Usamos la función creada previamente
            st.success(f"Archivo {archivo_imagen.name} cargado exitosamente")

    elif eleccion=='Conjuntos de datos':
        st.subheader("Conjunto de datos")
        archivo_datos = st.file_uploader('Subir CSV o Excel',type=['csv','xlsx']) #Definimos tipo de archivos
        if archivo_datos is not None:
            detalles_archivo = {'nombre': archivo_datos.name,
                                'tipo': archivo_datos.type,
                                'tamaño': archivo_datos.size}
            st.write(detalles_archivo)
            if detalles_archivo['tipo'] == "text/csv":
                df = pd.read_csv(archivo_datos)
            elif detalles_archivo['tipo'] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                df = pd.read_excel(archivo_datos)
            st.dataframe(df) #Insertamos el dataframe
            st.success(f'Archivo {archivo_datos.name} cargado exitosamente ')
    else:
        st.subheader('Documentos')
        archivo_doc = st.file_uploader("Subir documento",type=['docx','pdf','txt'])
        if st.button("Procesar"): #Insertamos botón
            if archivo_doc is not None:
                detalles_archivo = {'nombre':archivo_doc.name,
                                    'tipo': archivo_doc.type,
                                    'tamaño': archivo_doc.size}
                st.write(detalles_archivo)
                #Insertamos el contenido de aacuerdo a el tipo de documento
                if detalles_archivo['tipo'] == "text/plain":
                    texto = str(archivo_doc.read(),'utf-8')
                    st.write(texto) #Insertamos texto
                elif detalles_archivo['tipo'] == "application/pdf":
                    texto = leer_pdf(archivo_doc)
                    st.write(texto)
                elif detalles_archivo['tipo']== "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                    texto = docx2txt.process(archivo_doc)
                    st.write(texto)
                st.success(f'Archivo {archivo_doc.name} cargado exitosamente ')


if __name__ == '__main__':
    main()

