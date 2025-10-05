import pandas as pd

serie = pd.Series(['Honda','Toyota','Nissan','Italika'])

serie_colores = pd.Series(['Rojo','Amarillo','Azul','Verde'])

data = pd.DataFrame({'Tipo de Auto':serie,'Color':serie_colores})
serie_banderas = pd.Series(['EUA','mexico','Canadá'])
serie_lugar = pd.Series(['Este','Oeste','Centro'])
data_pais = pd.DataFrame({'Países':serie_banderas,'Lugar':serie_lugar})

#DataFra,es combinados
combinados = pd.concat([data_pais,data])

#creamos un dataframe con información de estudiantes
df_info= pd.DataFrame({'id':[1,2,3],'nombre':['Juanito','Roberto','Oziel'],'nota':[3,6,8]})
df_extra = pd.DataFrame({'id':[1,2,4],'club':['Boxeo','Ajedrez','Basketball']})
print(df_info)
print('-'*35)
print(df_extra)
print('-'*35)
df_combinados = pd.concat([df_info,df_extra]) #Combinamos los DataFrame
df_final = pd.merge(df_info,df_extra,on='id',how='left')
print(df_final) #Otra forma de combinarlos