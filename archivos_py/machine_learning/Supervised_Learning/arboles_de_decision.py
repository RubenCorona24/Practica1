#Importampos librerias
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,plot_tree #El modelo de arbol y la visualizacion
from sklearn.model_selection import train_test_split #libreria para separar las variables
from sklearn.preprocessing import LabelEncoder
import pandas as pd

#cargamos el dataset de "iris" de seaborn
data = sns.load_dataset('iris')
df = pd.DataFrame(data)
print(df)

#Separamos las variables 
X = df.drop('species',axis=1) #axis: indica que es una sola columna
le = LabelEncoder()
y = le.fit_transform(df.species)

#Separamos con train_test_split
X_entrena,X_prueba,y_entrena,y_prueba = train_test_split(X,y,test_size=0.8,random_state=42)
#train_size = 0.8: que el tamaño de la muestra sea igual al 80 porciento(entrenamiento), 20 porciento a la prueba
#random_state: controla la aleatoriedad que se distribuyen los registros, en este caso, la division que se haga de los datos cada que se reproduzca, será siempre la misma

#Creamos el arbol de decision con DecisionTreeClassifier()
arbol =  DecisionTreeClassifier()
arbol.fit(X_entrena,y_entrena) #Entrenamos al modelo

#Visualizamos el arbol con plot, con los argumentos necesarios
plt.figure(figsize=(8,8))
plot_tree(decision_tree=arbol,
          filled=True,
           class_names=['setosa','versicolor','virginica'],
           feature_names=df.columns.to_list())
plt.title("ÁRBOL DE DECISIÓN DE CLASES DE PLANTAS")
plt.savefig("archivos_aparte/data_sns/arbol_de_decision_plantas.png")
plt.show() #Mostramos el modelo

#Filled = True: rellena en colores por clase
#class_names: agrega nombre a cada clase
#feature_names: visualizamos las columnas por su nommbre en vez de la indexación

#OTRO EJEMPLO DE ESTE ALGORITMO
data2 = {
    'Edad': [22, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'Salario': [25000, 30000, 35000, 40000, 50000, 60000, 65000, 70000, 80000, 90000],
    'Compra': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
}

df2 = pd.DataFrame(data2)
#separar las variables
X = df2[['Edad','Salario']]
y = df2['Compra']
#Dividir los datos en %80 entrenamiento y %20 prueba
X2_entrena,X2_prueba,y2_entrena,y2_prueba = train_test_split(X,y,train_size=0.8,random_state=42)
#entrenamos el modelo 2
model2 = DecisionTreeClassifier(max_depth=5)
model2.fit(X2_entrena,y2_entrena)
#--------------------Evaluar el modelo con los datos de prueba-------------------------
score = model2.score(X2_prueba,y2_prueba)
print(f"Precisión del modelo: {score:.2f}")
#Visualizar el segundo arbol de decision
plt.figure(figsize=(8,8))
plot_tree(decision_tree=model2,
          filled=True,
          class_names=['No compra','Compra'],
          feature_names=['Edad','Salario'])
plt.title("ÁRBOL DE DECISION DE PROBABILIDADES DE COMPRA EN EDAD/SALARIO",fontsize=16)
plt.show() #Mostramos el árbol de decision

#La máxima precisión que puede alcanzar un modelo es de 1.0
