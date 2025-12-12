#Anonimización
#Proteger la identidad de las personas de un conjunto de datos sin perder utilidad en el análisis
import pandas as pd
import numpy as np
#Creamos un df con datos sensibles
data = pd.DataFrame({
    'nombre': ['Carlos','Maria','Elizabeth','Vanessa','Yohan'],
    'email': ['carlos@ejemplo.com','maria@ejemplo.com','eliza@ejemplo.com','vanes@ejemplo.com','yohan@ejemplo.com'],
    'edad': [22,27,48,55,63],
    'ubicación': ['Ciudad A','Ciudad B','Ciudad C','Ciudad D','Ciudad E'],
    'salario': [22600,45360,55400,35400,28000],
    'Banco': ['Banco 1','Banco 3','Banco 1','Banco 2', 'Banco 3']
})
#1.- Quitar las columnas nombres y email con df.drop()
data.drop(['nombre','email'],axis=1,inplace=True) #inplace:True para que sea permanente
#Anonimización de edades por redondeo
data['edad'] = (data['edad']//10) * 10
#3.- Ruido aleatorio: añadir ruido aleatorio a datos numéricos para desvincularlos de su valor real; el conjunto de datos preserva la utilidad estadística - mantiene propiedades generales
ruido = np.random.normal(0,100,size=data['salario'].shape) #Salario: la columna en la que quiero agregar ruido
data['salario'] +=ruido
#4 Permutación (shuffling): cambiar el orden datos(se pierde la relación que tiene con otros bancos del dataset) ejemplo con el banco
data['Banco'] = np.random.permutation(data['Banco'])

#Visualizamos el df después de los cambios
print(f"df modificado: \n{data}")