#Modificar el código de forma optimizada utilizando 
#StandardScaler, SelectKBest,Pipeline,cross_val_score
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split,cross_val_score #Entrenamiento y prueba
from sklearn.ensemble import RandomForestClassifier #Modelo de clasificación
#Nuevas librerias (optimización)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest,f_classif


# Cargar el dataset de diabetes
diabetes = datasets.load_diabetes()

# Convertir a DataFrame para facilitar el análisis exploratorio
diabetes_df = pd.DataFrame(data=np.c_[diabetes['data'], diabetes['target']],
                           columns=diabetes['feature_names'] + ['target'])

# Convertir 'target' en categorías para clasificación
diabetes_df['target'] = (diabetes_df['target'] > diabetes_df['target'].median()).astype(int)

# División de datos en conjuntos de entrenamiento y prueba
X = diabetes_df.drop('target', axis=1)
y = diabetes_df['target']
X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)


#----------------Modificación con pipeline para optimizar el proceso--------------------
pipeline =Pipeline([
    ('scaler',StandardScaler()),
    ('selector',SelectKBest(f_classif,k=5)),
    ('modelo',RandomForestClassifier(n_estimators=100, random_state=42))
])

#Entrenamos el pipeline con el fin de ejecutar cada proceso
pipeline.fit(X_entrena,y_entrena)

# Realizar predicciones con el conjunto de prueba
predicciones = pipeline.predict(X_prueba)

# Evaluación del modelo (muestra de precisión y predicciones)
puntaje = pipeline.score(X_prueba,y_prueba)
print(f"\nPrecisión del modelo: {puntaje}")
puntajes_validacion_cruzada = cross_val_score(pipeline,X,y,cv=5)
print(f"Puntajes de validación cruzada: {puntajes_validacion_cruzada}\n")
print(f"Promedio de puntuación de validación cruzada: {np.mean(puntajes_validacion_cruzada):.2f}\n")
print(f"Predicciones: {predicciones}")