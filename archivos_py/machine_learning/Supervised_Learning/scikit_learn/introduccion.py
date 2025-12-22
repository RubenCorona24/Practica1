#Componentes de Sklearn:
#- **Estimadores:** objetos que aprenden de datos usando el método *.fit()*
#- **Transformadores:** estimadores que modifican los datos, usan *.fit()* para aprender como transformar, usan **.transform()** para aplicar la transformación
#- **Predictores:** Estimadores que hacen predicciones, usan *.predict()*, y a veces *.predict_proba()*, todos los modelos supervisados son predictores.

#Ejemplo de código con sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

#Cargamos el dataset
iris = load_iris()
#Dividimos en variables dependientes e independientes
X = iris.data
y = iris.target
#Dividimos el dataset en entrenamiento/prueba
X_entrena,X_prueba,y_entrena,y_prueba = train_test_split(X,y,test_size=0.3,random_state=42)
#Creamos una instancia del escalador
scaler = StandardScaler()
#Estimador (StandarScaler): Aprendemos los parámetros de escalado con fit
scaler.fit(X_entrena)
#Estimador (StandarScaler): Aplicamos la transformación a los datos de entrenamiento y prueba
X_entrena_escalado = scaler.transform(X_entrena)
X_prueba_escalado = scaler.transform(X_prueba)
#Creamos el modelo LogisticRegression
modelo = LogisticRegression()
#Estimador (LogisticRegression): Entrenamos el modelo con los datos escalados
modelo.fit(X_entrena_escalado,y_entrena)
#Predictor (LogisticRegression): Hacemos predicciones y evaluamos el modelo
y_pred = modelo.predict(X_prueba_escalado)
puntaje = modelo.score(X_prueba_escalado,y_prueba)
print(f"Las predicciones son: {y_pred}")
print(f"El puntaje del modelo es: {puntaje :.2f}")

#- Estimadores: StandardScaler, LogisticRegression
#- Transformadores: StandardScaler
#- Predictores: LogisticRegression