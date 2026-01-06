#Comprobar el desempeño de un modelo antes de aplicarlos a nuestros datos por medio de la validación cruzada "**cross_val_score**"x|
#Importamos librerías
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score #Método de validación cruzada para evaluar el desempeño del modelo

#Cargamos datos
data = load_iris()
X = data.data
y = data.target

#Creamos el modelo
modelo = RandomForestClassifier(n_estimators=100,random_state=42)

#Variable que contiene la evaluación con cross_val_score
puntaje = cross_val_score(modelo,X,y,cv=5) #Pasamos de argumentos: el modelo, las variables y el número de iteraciones en los datos
print(f"Exactitud de cada partición: {puntaje}")
print(f"Exactitud promedio: {puntaje.mean()}")

#La función de cross_val_score ejecuta automáticamente el proceso de entrenamiento y evaluación del modelo mediante la validación cruzada. Devuelve un array donde contiene la métrica de rendimiento.