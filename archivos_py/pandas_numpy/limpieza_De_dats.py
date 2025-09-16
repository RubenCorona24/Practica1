import pandas as pd
df = pd.read_csv("archivos_aparte//archivo_incompleto.csv")
print(df)
print("---------------Vemos los valores nulos con isnull()----------------\n")
nulos = df.isnull().sum()
print(f"Valores nulos:\n{nulos}")
#Limpiar datos con dropna
print("---------------Valores eliminados ----------------\n")
df_limpio = df.dropna()
print(df_limpio)
print("---------------Valores rellenados ----------------\n")
valores_nuevos = {'precio':df['precio'].mean()}
df_rellenados = df.fillna(valores_nuevos)
print(df_rellenados)
df_rellenados['cantidad'] = df_rellenados['cantidad'].astype(int)
print("---------------Modificamos los valores de cantidad para que ahora sean integer ----------------\n")
print(df_rellenados)
print("---------------Valores duplicados eliminados----------------\n")
df_unicos = df_rellenados.drop_duplicates(subset="id producto") #solo se fija en la columna id producto
print(df_unicos)
print("--------------Parte de series filtradas----------------\n")


#Filtración de series
serie = pd.Series([1,5,10,15,20,25])
filtro = serie >15  #aplicamos el filtro
serie_filtrada = serie[filtro] #creamos una nueva serie con el filtro
print(f"La serie inicial:\n{serie}\n")
print(f"El filtro de la serie:\n{filtro}\n")
print(f"Nueva serie con filtro:\n{serie_filtrada}")
print("--------------Filtrar series de strings----------------\n")
serie2 =  pd.Series(['banana','manzana','mandarina','limón','mango'])
filtro2 = serie2.str.contains('m')
serie2_filtrada = serie2[filtro2]
print(f"Segunda serie inicial:\n{serie2}\n")
print(f"Filtro de la serie:\n{filtro2}\n")
print(f"Segunda serie filtrada:\n{serie2_filtrada}\n")
print("--------------Agregación de series----------------\n")
new_serie = pd.Series([10,20,30,40,50])
promedio = new_serie.mean()
print(f"Mi nueva serie es:\n{new_serie}\n")
print(f"El promedio de mi serie es: {promedio}")
suma = new_serie.sum()
print(f"La suma de mi serie es: {suma}")
maximo,minimo = new_serie.max(),new_serie.min()
print(f"El máximo de mi serie es: {maximo}, y el mínimo {minimo}")

