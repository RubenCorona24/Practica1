import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model #Importamos linear model desde sklearn
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