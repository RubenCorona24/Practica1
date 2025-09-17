import pandas as pd
df = pd.read_csv("archivos_aparte//medallas.csv")
print("-"*20 + "Análisis de medallas en diferentes paises" + "-"*20 + "\n")
print(df)
print(f"Datos de filas y columnas: {df.shape}\n")
print(f"Primeros 5 países:\n{df.head()}\n") #Mostrar primeros 5 países
print(f"Últimos 5 países:\n{df.tail()}\n") #Mostrar últimos 5 países
datos_nulos = df.isnull().sum()
mas_nulos = datos_nulos.idxmax()
print(f"Los datos nulos de el dataframe son:\n{datos_nulos}\nEl dato más nulo es: {mas_nulos}")
df_limpio = df.dropna()
print(f"----------Dataframe limpio sin datos nulos-----------:\n{df_limpio}\n")
print(f"Ahora los datos nulos de este data son:\n{df_limpio.isnull().sum()}\n")
promedio_oro = df['Oro'].mean()
promedio_plata = df['Plata'].mean()
promedio_bronce = df['Bronce'].mean()
valores_reemplazo = {
    'Oro': promedio_oro,
    'Plata': promedio_plata,
    'Bronce': promedio_bronce
}  #Crear un diccionario con los valores de reemplazo
df_rellenado= df.fillna(valores_reemplazo) #Hacer un nuevo DataFrame rellenado con función fillna()
print(f"----------El nuevo DataFrame con datos rellenados por promedio------:\n{df_rellenado}\n")
print(f"Valores nulos de este DataFrame:\n{df_rellenado.isnull().sum()}\n")
#Transformar los datos de tipo float a str
df_rellenado = df_rellenado.astype(int, errors='ignore') #errors='ignore' evita error si una columna no puede convertirse, como País
print(f"------DataFrame con datos enteros-----:\n{df_rellenado}\n")

#Análisis de medallas de oro por país
def analizar_medallas_paises(data):
    print("-------TOP 3 DE CADA MEDALLA---------\n")
    top_3_oro = df.sort_values('Oro',ascending=False).head(3)
    print(f"Medallas de oro:\n{top_3_oro}\n") #Muestra los 3 primeros países ocn más medallas oro
    top_3_plata = df.sort_values('Plata',ascending=False).head(3)
    print(f"Medallas de plata:\n{top_3_plata}\n") #Muestra los 3 primeros países ocn más medallas plata
    top_3_bronce = df.sort_values('Bronce',ascending=False).head(3)
    print(f"Medallas de bronce:\n{top_3_bronce}\n") #Muestra los 3 primeros países ocn más medallas bronce
analizar_medallas_paises(df_rellenado)

#Análisis de medallas totales por país
def medallas_totales(df):
    print("----------Países con más de 10 medallas---------\n")
    filtro = df['Total'] > 10
    mas_10_medallas = df[filtro]
    mas_medallas = df.loc[df['Total'].idxmax()]['Pais']
    print(mas_10_medallas.sort_values('Total',ascending=False))
    print(f"Páis con más medallas en total: {mas_medallas}")

medallas_totales(df_rellenado)