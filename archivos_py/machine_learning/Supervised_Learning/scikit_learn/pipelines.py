#Un Pipeline es una herramienta de Scikit-Learn que permite encadenar varios pasos de procesamiento y modelado en un solo flujo automático.
#Cada paso se ejecuta en orden, desde el preprocesamiento de datos hasta el entrenamiento y la predicción del modelo.
#Un Pipeline combina:
#Transformadores → modifican los datos (StandardScaler, OneHotEncoder, etc.)
#Estimador final → modelo que aprende (LogisticRegression, SVM, RandomForest, etc.)
#Importamos librerías
from sklearn.datasets import load_iris #El dataset con el que trabajamos
from sklearn.model_selection import train_test_split #Dividir el dataset en train y test
from sklearn.preprocessing import StandardScaler #El transformador de datos
from sklearn.linear_model import LogisticRegression #El estimador final
from sklearn.pipeline import Pipeline #El pipeline

#Cargamos dataset
data = load_iris()
#Dividimos las variables dependientes e independientes
X = data.data
y = data.target

#Dividimos el dataset en conjuntos de entrenamiento y prueba con train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#--------CREAMOS EL OBJETO PIPELINE---------------
pipeline = Pipeline([
    ('scaler',StandardScaler()),
    ('modelo',LogisticRegression())
])
#Entrenamos solo al pipeline que va a escalar y entrenar
pipeline.fit(X_train,y_train)


#Realizamos predicciones en el conjunto de prueba
y_pred = pipeline.predict(X_test)
puntaje =pipeline.score(X_test, y_test)
print("Puntuación del modelo:", puntaje)
print("Predicciones:", y_pred)
print("Valores reales:", y_test)
