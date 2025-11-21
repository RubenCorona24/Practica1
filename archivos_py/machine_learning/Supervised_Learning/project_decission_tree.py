#PROYECTO CON EL ALGORITMO ÁRBOL DE DECISIÓN
#Proyecto que deduce si el estudiante aprueba o no en base a sus horas de estudio, asistencias, y calificaciones
import pandas as pd
from sklearn.tree import DecisionTreeClassifier,plot_tree #Importamos las librerías para el modelo
import matplotlib.pyplot as plt #Librería para visualizar datos
from sklearn.model_selection import train_test_split
datos = {
    "horas_estudio": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "tareas_entregadas": [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
    "asistencias": [60, 65, 70, 75, 80, 85, 90, 92, 95, 98],
    "aprobo": ["No","No","No","Sí","Sí","Sí","Sí","Sí","Sí","Sí"]
}

df = pd.DataFrame(datos) #Convertimos data en un df

#Dividimos las variables
X = df.drop('aprobo',axis=1)
y = df['aprobo']
X_entrena,X_prueba,y_entrena,y_prueba = train_test_split(X,y,random_state=42,train_size=0.8) #Dividimos en entrenamiento y prueba

#creamos el modelo de arboles de decision
arbol = DecisionTreeClassifier(max_depth=4)
arbol.fit(X_entrena,y_entrena) #Entrenamos a nuestro modelo con las variables entrenadas

#Visualizamos la precisión del modelo
score = arbol.score(X_prueba,y_prueba)
print(f"El puntaje de precisión del modelo es: {score:.3f}") #Lo dejamos en 3 decimales


#Visualizamos el arbol
plt.figure(figsize=(10,6))
plot_tree(arbol,filled=True,feature_names=df.columns.to_list(),class_names=['Aprobó','No aprobó']) 
plt.show()

#Hacemos una prediccion con nuevos datos
news = pd.DataFrame({
    "horas_estudio": [8, 2],
    "tareas_entregadas": [6, 4],
    "asistencias": [90, 95]
})

predict = arbol.predict(news)
print(F"Predicción para los nuevos estudiantes:\n{news}\nResultado:{predict}")
