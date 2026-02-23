#---------------PROYECTO DE STUDENTS DATASET MACHINE LEARNING WITH RANDOMFORESTREGRESSOR---------------

#Importamos librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\coron\Downloads\student_dataset.csv")
print(df.head())
#Hacemos visualizaciones de distintas columnas y mostrar sus relaciones
plt.figure(figsize=(12,6))
sns.barplot(df,x=df['age'],y=df['study_hours_per_day'],hue='gender') #Dividimos el género
plt.title("Relación Edad - Horas de Estudio")
plt.xlabel("Edad")
plt.ylabel("Horas de estudio")
plt.show()

#Relación uso de teléfono con notas finales
plt.figure(figsize=(12,6))
plt.scatter(df['phone_usage_hours'].head(30),df['final_grade'].head(30),color='red')
plt.title("Relación uso de teléfono - Notas finales")
plt.xlabel("Horas de uso de teléfono")
plt.ylabel("Notas finales")
plt.show()

#Entrenamos un modelo (RandomForestRegressor) para visualizar las importancias
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

modelo = RandomForestRegressor(n_estimators=100,random_state=42)
#Dividimos datos dependientes e independientes
X = df.drop(["student_id", "gender", "productivity_score"], axis=1)
y = df['productivity_score'] #El resultado

#Dividimos datos en entrenamiento y prueba
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

#Entrenamos el modelo
modelo.fit(X_train,y_train)

#Visualizamos el score del modelo
score = modelo.score(X_test,y_test)
print(f"Puntaje del modelo: {score:.3f}") #3 decimales


#Después de entrenar al modelo sacamos las importancias
importancias = modelo.feature_importances_
r = pd.DataFrame({
    'Features': X.columns,
    'Importance': importancias
}).sort_values('Importance',ascending=False)

#Graficamos las importancias del modelo
plt.figure(figsize=(12,6))
sns.barplot(x='Importance',y='Features',data=r)
plt.title("Importancia de Las Características")
plt.xlabel("Importancia")
plt.ylabel("Características")
plt.show()
