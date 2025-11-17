import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
#----PRIMER EJEMPLO DE COMO FUNCIONA SVD-------
def svd_array():
    A = np.array([[1,2],[3,4],[5,6]]) #creamos un array bidimensional
    #creamos las 3 matrices
    U,sigma,Vt = np.linalg.svd(A) #Pasamos como argumento A
    #Visualizamos los resultados de cada matriz
    print(f'U: {U}\nsigma:{sigma} \nVT:{Vt}')

#----SEGUNDO EJEMPLO DE COMO FUNCIONA SVD-------
def svd(A):
    U,sigma,Vt = np.linalg.svd(A)
    print(f'U: {U}\nsigma:{sigma} \nVT:{Vt}')
    return U,sigma,Vt #La función devuelve las 3 matrices
#cargamos el dataset
iris = load_iris()
X = iris.data #extraemos solo el target del dataset
#Centramos los datos
X_centrado = X - np.mean(X,axis=0)
U,sigma,Vt = svd(X_centrado) #Llamamos a la función

k=2 #Definimos que son solo 2 elementos
X_transformado = U[:,:k] * sigma[:k] #Reducimos la dimensionalidad de un conjunto de datos
#---Visualización de los resultados-------
especies = ['setosa','versicolor','virginica'] #Definimos las especies en una lista
plt.figure(figsize=(10,6)) #Configuramos el tamaño de la figura
for i in range(3):
    plt.scatter(X_transformado[iris.target==i,0],X_transformado[iris.target==i,1],label=especies[i]) #label=especies: definimos las etiquetas con sus respectivas especies
    plt.xlabel("Componente principal 1")
plt.ylabel("Componente principal 2")
plt.legend() #Nos aseguramos que el gráfico tenga leyenda
plt.title("Dataset Iris transformado por SVD")
plt.show()

