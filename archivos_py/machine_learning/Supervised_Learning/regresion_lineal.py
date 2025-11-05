#Regresión Lineal: lgoritmo de aprendizaje supervisado que se utiliza para predecir un valor continuo (variable dependiente) basándose en una o más variables independientes. 
#Se basa en ajustar una línea recta que mejor se adapte a los datos, minimizando el error entre los valores predichos y reales,
#con el objetivo de modelar la relación entre las variables. 

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model #Importamos linear model desde sklearn
import random
#Creamos un df (columna precio y columna area)
df = pd.DataFrame({
    'Area': [26000,30000,32000,36000,40000],
    'Precio': [550000,565000,610000,680000,725000]
})

def graficar():
    plt.scatter(df['Area'],df['Precio'])
    plt.show()
graficar()
#Creamos una variable llamada X: donde le pasamos el "Dataframe" de area, por lo tanto es bidimensional
X = df[['Area']]
#Creamos una variable llamada y: le pasamos el precio y SI es una serie
y = df['Precio']
#Creamos el modelo con linear_model.Linear_Regression()
modelo = linear_model.LinearRegression()
#Entrenamos al modelo con: modelo.fit()
modelo.fit(X,y)
#Hacemos primero una predicción aleatoria de el area
print(modelo.predict([[3300]]))
#Creamos el gráfico con las predicciones del modelo
plt.plot(df['Area'],modelo.predict(X)) #como parámetro eje y, en vez de poner a "y", pasamos el modelo.predict pero con parametro de X
plt.title("Gráfica con modelo entrenado")
plt.xlabel("Area de la casa")
plt.ylabel("Precio ($)")
plt.show()

#Otroo ejemplo de regresión lineal
#Predicción del Precio de una casa según su tamaño
df = pd.DataFrame({
    'Tamaño': [50,60,80, 100,120],
    'Precio(USD)': [150000,180000,240000,300000,360000]
})

def entrenar_modelo():
    X2 = df[['Tamaño']]
    y2 = df['Precio(USD)']
    model = linear_model.LinearRegression()
    model.fit(X2,y2) #Entrenamos al modelo
    size_aleatorio = random.randint(120,200)
    print(f"Costo del tamaño de {size_aleatorio}m²: {model.predict([[size_aleatorio]])[0]:.2f}")
    return X2,y2,model

X2,y2,model = entrenar_modelo()
def graficar_modelo(X,y):
    plt.scatter(X,y,color='blue',marker='o',label='Data Real') 
    plt.plot(X,model.predict(X),color='red',marker='+',label='Model predictions')
    plt.xlabel('Tamaño en Metros cuadrados')
    plt.ylabel("Precio (USD)")
    plt.show()   
graficar_modelo(X2,y2) #Llamamos a la función de graficar el modelo