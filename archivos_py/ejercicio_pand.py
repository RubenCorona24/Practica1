import pandas as pd

serie = pd.Series(['Honda','Toyota','Nissan','Italika'])

serie_colores = pd.Series(['Rojo','Amarillo','Azul','Verde'])

data = pd.DataFrame({'Tipo de Auto':serie,'Color':serie_colores})
serie_banderas = pd.Series(['EUA','mexico','Canadá'])
serie_lugar = pd.Series(['Este','Oeste','Centro'])
data_pais = pd.DataFrame({'Países':serie_banderas,'Lugar':serie_lugar})
print(data_pais)
#DataFra,es combinados
combinados = pd.concat([data_pais,data])
print(combinados)