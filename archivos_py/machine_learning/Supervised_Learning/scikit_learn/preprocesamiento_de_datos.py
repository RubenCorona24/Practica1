#El preprocesamiento prepara los datos para que los modelos de Machine Learning:
#- 🧠 Aprendan mejor
#- ⚖️ No se vean afectados por escalas distintas
#- 🚫 No fallen por datos faltantes o mal formateados
#- 📈 Obtengan mejores predicciones
#El preprocesamiento transforma los datos crudos en datos adecuados para entrenar modelos.

#Importamos librerías
import numpy as np
from sklearn.preprocessing import MinMaxScaler,StandardScaler,OneHotEncoder #Para preprocesamiento de datos
from sklearn.datasets import load_iris #Para cargar un dataset

data = np.array([[1,-1,2],[2,0,0],[0,1,-1]])#Datos de ejemplo
data
#Utilizamos MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1)) #Establecemos el rango entre 0 y 1
data_escalada = scaler.fit_transform(data) #Escalamos los datos
data_escalada

iris = load_iris() #Cargamos dataset
#Separamos la variable independiente
X = iris.data
#Establecemos scaler y transformamos
scaler = MinMaxScaler(feature_range=(0,1)) #Establecemos el rango entre 0 y 1
X_escalado = scaler.fit_transform(X) #Escalamos los datos
print(X[:5]) #Primeras 5 filas de X
print(X_escalado[:5]) #Primeras 5 filas de X escalado

scaler2 = StandardScaler()
data_escalada2 = scaler2.fit_transform(data)
data_escalada2
print(np.std(data_escalada2)) #1
print(np.mean(data_escalada2)) #0

#Creamos array con características de colores
categorias = np.array([['rojo'],['verde'],['azul'],['rojo'],['verde'],['azul']])
categorias

encoder = OneHotEncoder(sparse_output=False) #Matrices dispersas
#Codificamos los datos
data_codificada = encoder.fit_transform(categorias)
data_codificada #Salida de array de 6 flas - código binario para cada elemento único "3 únicos (rojo,verde, y azul)"