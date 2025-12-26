#El ajuste de hiperparámetros con GridSearchCV es un método exhaustivo para seleccionar el modelo
#  más óptimo mediante la evaluación sistemática de todas 
# las combinaciones posibles de un conjunto de valores de hiperparámetros

#Importamos librerías
from sklearn.datasets import load_iris #El dataset que utilizamos
from sklearn.ensemble import RandomForestClassifier #El modelo clasificador
from sklearn.model_selection import GridSearchCV #Ajustar hiperparámetros
#Cargamos dataset y dividmos variables dependientes e independientes
data = load_iris()
X = data.data
y = data.target
#Instanciamos el modelo
modelo= RandomForestClassifier(random_state=42)
#Instanciamos los parámetros posibles del modelo en un diccionario
parametros = {
    'n_estimators': [50,100,200],
    'max_features': ['sqrt','log2'],
    'max_depth': [4,5,6,7,8],
    'criterion': ['gini','entropy']
}
#Instanciar el grid pasando los argumentos el modelo, los parámetros y el cv (las veces de repaso)
grid = GridSearchCV(modelo,parametros,cv=5,scoring='accuracy')
#Entrenamos el search con .fit() pasando de argumentos a X e y
grid.fit(X,y)
#Una vez entrenada visualizamos los resultados de los mejores parámetros para el modelo con .best_params_ y la exactitud con .best_score_
print(f"Mejores parámetros del modelo: {grid.best_params_}")
print(f"Exactitud: {grid.best_score_}")