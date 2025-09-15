import pandas as pd
df = pd.read_csv("archivos_aparte//archivo_incompleto.csv")
print(df)
print("---------------Vemos los valores nulos con isnull()----------------")
nulos = df.isnull().sum()
print(f"Valores nulos: {nulos}")
#Limpiar datos con dropna
print("---------------Valores eliminados ----------------")
df_limpio = df.dropna()
print(df_limpio)
print("---------------Valores rellenados ----------------")
valores_nuevos = {'precio':df['precio'].mean()}
df_rellenados = df.fillna(valores_nuevos)
print(df_rellenados)
df_rellenados['cantidad'] = df_rellenados['cantidad'].astype(int)
print("---------------Modificamos los valores de cantidad para que ahora sean integer ----------------")
print(df_rellenados)
print("---------------Valores duplicados eliminados----------------")
df_unicos = df_rellenados.drop_duplicates(subset="id producto") #solo se fija en la columna id producto
print(df_unicos)