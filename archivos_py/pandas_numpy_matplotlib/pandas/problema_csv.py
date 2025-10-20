#Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv('archivos_aparte\\daos.csv') #Leer el archivo csv

#reemplazando los datos "Corona" por "Mendoza"
df['apellido'].replace('Corona','Mendoza',inplace=True)

#Convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#eliminando las filas con datos faltantes
df = df.dropna()

#eliminando las filas repetidas
df = df.drop_duplicates()

#Creando un CSV con el dataframe resultante (limpio)
df.to_csv('archivos_aparte\\datos_limpios.csv')
