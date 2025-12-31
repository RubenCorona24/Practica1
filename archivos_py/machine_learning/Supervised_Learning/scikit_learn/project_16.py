#Importamos librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine #Dataset
from sklearn.model_selection import train_test_split #División entrenamiento y prueba
from sklearn.preprocessing import StandardScaler #Escalador - transformador de datos
from sklearn.linear_model import LogisticRegression #Modelo - estimador
from sklearn.pipeline import make_pipeline #Utilizamos pipeline
wine_data = load_wine()
df = pd.DataFrame(data=np.c_[wine_data['data'], wine_data['target']],
                  columns=wine_data['feature_names'] + ['target'])

print(df.head(5))
print(df.tail(5))

#Visualizaciones con matplotlib
plt.figure(figsize=(6,10))
plt.hist(df['magnesium'])
plt.title("Distribución de magnesio en el vino")
plt.xlabel("Cantidad de magensio")
plt.ylabel("Distribución")
plt.show() #Mostrar el histograma
#Scatterplot
fig,ax = plt.subplots()
ax.scatter(df['alcohol'],df['malic_acid'],c='red',s=100)
ax.set(title='Relación entre cantidad e alcohol y acidez',xlabel='Cantidad alcohol',ylabel='Acidez')
plt.show()
#Conclusión: En general, la mayor acidez se encuentra cuando la cantidad de alcohol está entre 12 y 14

#Preparación de datos
#Dividimos variables dependientes e independientes
X = wine_data.data
y = wine_data.target
#División de datos en entrenamiento y prueba con train_test_splot
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.25,random_state=42)

#Uso del pipeline: preprocesamiento de datos, entrenamiento del modelo
pipeline = make_pipeline(StandardScaler(),LogisticRegression())
pipeline.fit(X_train,y_train) #El pipeline transforma los datos y entrena el modelo

#Evaluación del modelo
score = pipeline.score(X_test,y_test)
predictions = pipeline.predict(X_test)

print(f"Precisión del modelo: {score:.2f}") #Dejamos en 2 decimales
print(f"Predicciones del modelo: {predictions}")

#Conclusiones: score del modelo: 0.93 - Es confiable
# Predicciones del modelo: [0 0 2 0 1 0 1 2 1 2 0 2 0 1 0 1 1 1 0 1 0 1 1 2 2 2 1 1 1 0 0 1 2 0 0 0 2 2 1 2 0 1 1 2 2 0 1 1 2 0 1 0 0 2 2 1 0 0 1 0 2 1 0 2 0 0 0 2 0 0 0 2 1 0
#2 1 0 2 1 1 0 2 0 0 1 0 0 2 1 1 1 0 1 1 1 2 2 0 1 2 2 2 0 0 1 2 2 1 2 1 1
# 1 0 0 2 0 2 0 0 1 1 0 0 0 1 0 2 2 1 1 2 2 2 1]





