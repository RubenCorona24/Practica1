#Importamos las librerias
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

#Libreria del modelo RandomForest
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler

#leemos el df

df = pd.read_csv("archivos_aparte/archivos_csv/tarjetas_credito.csv")
print(df.head()) #Leemos la cabezera del DataFrame

def escalar():

#Creamos una escala con MinMaxScaler()
    escala = MinMaxScaler()
    normado = escala.fit_transform(df) #normado: es el df transformado con el metodo escala.fit_transform
    df_normado = pd.DataFrame(data=normado,columns=df.columns) #Convertimos normado a un Dataframe
    #columns: el título de las columnas será el mismo (df.columns)
    print(df_normado)
    return df_normado

#separamos las variables independientes de las dependientes
df = escalar()
def separar_variables(df):
    X = df.drop('Clase',axis=1)
    #axis=1: indica que es una sola columna
    y = df.Clase
    return X,y
X,y = separar_variables(df)

#Dividir las variables en entrenamiento y prueba
def train_test(X,y):
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.8,random_state=42)
    return X_train,X_test,y_train,y_test
X_train,X_test,y_train,y_test = train_test(X,y)

#Crear el algoritmo de bosque aleatorio (RandomForestClassifier)
def model(X_train,X_test,y_train,y_test):
    forest = RandomForestClassifier() #Creamos el modelo forest
    entrenado = forest.fit(X_train,y_train) #Entrenamos al modelo con X_train,y_train
    #Visualizamos el puntaje del arbol (forest.score(X_prueba,y_prueba))
    accuracy = forest.score(X_test,y_test)
    print(F"Precisión del modelo: {accuracy:.2f}")
    return entrenado

entrenado = model(X_train,X_test,y_train,y_test)
#Cargamos un nuevo registro de dataset y mediante ello hacemos predicciones
new_data = pd.DataFrame({
    'Duracion': [0.000006], 'V1': [0.452345], 'V2': [0.564789], 'V3': [0.123456], 'V4': [0.654321],
    'V5': [0.987654], 'V6': [0.345678], 'V7': [0.234567], 'V8': [0.876543], 'V9': [0.456789],
    'V10': [0.567890], 'V11': [0.678901], 'V12': [0.789012], 'V13': [0.890123], 'V14': [0.901234],
    'V15': [0.012345], 'V16': [0.543210], 'V17': [0.432109], 'V18': [0.321098], 'V19': [0.210987],
    'V20': [0.109876], 'V21': [0.098765], 'V22': [0.887654], 'V23': [0.776543], 'V24': [0.665432],
    'V25': [0.554321],     'V26': [0.443210], 'V27': [0.332109], 'V28': [0.221098], 'Monto': [0.110987]
}, index=[0])

def predict(data):
    clase_predicha = entrenado.predict(data)
    #otra forma de predecir
    probabilidades = entrenado.predict_proba(data)
    print(f"Clase predicha: {clase_predicha[0]}") #Clase predicha, 0 o 1
    print(f"Probabilidades de Legitimidad: {probabilidades[0][0]}") #Probabilidades de Legitimidad
    print(f"Probabilidades de Fraude: {probabilidades[0][1]}") #Probabilidades de fraude

predict(new_data)

#RESULTADO DE DATOS
#Clase predicha: 0.0
#Probabilidades de Legitimidad: 0.61
#Probabilidades de Fraude: 0.39
#--------MÁS PROBABILIDADES DE LEGITIMIDAD, PERO SIGUE SIENDO INCIERTO------------