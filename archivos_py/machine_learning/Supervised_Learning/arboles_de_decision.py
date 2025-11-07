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