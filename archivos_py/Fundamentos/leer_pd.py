import pandas as pd #Importamos la librería pandas
df = pd.read_csv('archivos_aparte\\daos.csv') #Usando la función read_csv para leer el archivo CSV
df2 = pd.read_csv('archivos_aparte\\daos.csv') 

#Método slycing
numeros = '0123456'
print(numeros[0:6])

nombres = df["Nombre"] #Obteniendo los datos de la columna nombre

df_ordenado = df.sort_values('edad') #ordenando del dataframe por edad

df_ordenado_inverso = df.sort_values('edad',ascending=False ) #ordenando de forma descendente

df_concatenado = pd.concat([df,df2]) #Concatenando los dos dataframes

primer_fila = df.head(1) #Accediendo a la primer fila con head()
filas_columnas_totales = df.shape
df_info = df.describe() #Obteniendo data estadística del dataframee
elemento_especifico = df.loc[2,'edad'] #Accediendo a la edad de la fila 2 con loc[]
apellidos = df.iloc[:,1] #Accediendo a todas las filas de una columna   
mayor_30 = df.loc[df['edad']>30,:] #Accediendo a filas con edad mayor que 30

print("------------------------------dataframe")
print(df_ordenado)
print("------------------------------dataframe inverso")
print(df_ordenado_inverso)
print("------------------------------dataframes concatenados")
print(df_concatenado)
print("------------------------------Primer fila dataframe")
print(primer_fila)
print("------------------------------Filas y columnas totales")
print(filas_columnas_totales)
print("------------------------------Apellidos")
print(apellidos)