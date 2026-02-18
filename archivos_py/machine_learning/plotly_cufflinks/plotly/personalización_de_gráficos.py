#Proyecto personal de visualización de datos con plotly
#--ANÁLISIS DE VENTAS GLOBALES ----
import pandas as pd
import  kagglehub
import numpy as np
import matplotlib.pyplot as plt

#Creamos el dataframe
df = pd.DataFrame({
    "fecha": pd.date_range(start="2024-01-01", periods=120),
    "ciudad": np.random.choice(["CDMX", "Bogotá", "Lima", "Buenos Aires"], 120),
    "producto": np.random.choice(["Laptop", "Tablet", "Celular"], 120),
    "categoria": np.random.choice(["Tecnología", "Accesorios"], 120),
    "ventas": np.random.randint(50, 500, 120),
    "ganancia": np.random.randint(20, 200, 120)
})

from functions import visualize,clean_df #Extraemos funciones 

visualize(df)

#Grafico de lineas de ventas en el tiempo
df['fecha'] =  pd.to_datetime(df['fecha'])
plt.plot(df["fecha"],df['ventas'])
plt.title('Ventas por el tiempo')
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.show()

#Gráfico de barras ventas por ciudad
plt.bar(df['ciudad'],df['ventas'],color='red')
plt.title('Ventas por Ciudad')
plt.xlabel("Ciudad")
plt.ylabel("Ventas")
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

X = df.drop('ventas')
y = df['ventas']
x_entrena,x_prueba,y_entrena,y_prueba = train_test_split(X,y,train_size=0.8,random_state=42)
modelo =LinearRegression()
modelo.fit(x_entrena,y_entrena)
score = modelo.score(x_prueba,y_prueba)
print(f"Precisión del modelo: {score:.2f}")
