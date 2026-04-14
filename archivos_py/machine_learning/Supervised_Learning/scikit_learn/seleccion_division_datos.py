#Importamos librerías
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, SelectFromModel,chi2

#cargamos el dataset iris
iris = load_iris()
#Dividimos los datos/objetivos de iris
X = iris.data
y = iris.target

# Dividimos los datos en entrenamiento y prueba mediante train_test_split

X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42) #Se divide 20% prueba y 80% entrenamiento
#Verificamos el tamaño de los datos divididos
print(f"Tamaño del conjunto total: {len(X)}")
print(f"Tamaño del conjunto de entrenamiento: {len(X_entrena)}")
print(f"Tamaño del conjunto de prueba: {len(X_prueba)}")

#2.- Selección de características: **SelectKBest** y **SelectFromModel** - identificar cuales son las características más importantes para hacer predicciones
#- SelectKBest: selecciona una cantidad determinada de características basadas en pruebas estadísticas univariadas - con el fin de reducir la dimensionalidad y simplificar el modelo
#- SelectFromModel: selecciona características por importancia - basadas en la importancia de las características asignadas por un *modelo* predictivo base

selector = SelectKBest(chi2,k=2) #Parámetros: métodos para el puntaje, num de características "k"
#Creamos un nuevo dataset mediante el selector
X_nuevo = selector.fit_transform(X_entrena,y_entrena) #Mediante el método .fit_transform - selección y transformación de datos
print(X_entrena[:5])
print(X_prueba[:5])

print(X_nuevo[:5]) #Las columnas más importantes

from sklearn.ensemble import RandomForestClassifier #Importamos modelo
modelo = RandomForestClassifier(n_estimators=100,random_state=42) #Creamos el modelo
selector2 = SelectFromModel(modelo) #Creamos selector pasando el modelo
X_nuevo2 = selector2.fit_transform(X_entrena,y_entrena) #Mediante el método .fit_transform - selección y transformación de datos
print(X_entrena[:5])
print(X_nuevo2[:5])