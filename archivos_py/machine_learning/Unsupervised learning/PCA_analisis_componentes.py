#PCA: Modelo de Machine Learning
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA #Nuestro modelo pca
from sklearn.datasets import load_iris #Dataset que vamos a utilizar
from sklearn.preprocessing import StandardScaler
iris = load_iris()
#Definimos las varuables dependientes e independientes (x,y)
X = iris.data #Los datos del dataset
y = iris.target #La parte del target
#Estandarizamos/normalizamos los datos
scale = StandardScaler() 
X_scaler = scale.fit_transform(X)#Creamos al modelo PCA
pca = PCA(n_components=2)#Definimos que trabajaremos con 2 componentes
X_pca = pca.fit_transform(X_scaler) #Entrenamos al modelo pasando datos normalizados
#Visualizamos los datos
plt.figure(figsize=(10,6))
plt.scatter(X_pca[:,0],X_pca[:,1],alpha=0.7,c='red',marker='x')
plt.title("PCA del conjunto Iris 1.0")
plt.xlabel("Primer componente principal")
plt.ylabel("Segundo componente principal")
plt.show()

#-----------SI QUEREMOS ESPECIFICAR LAS ESPECIES Y MOSTRAR ETIQUETAS SEGUIMOS ESTOS PASOS-----------
especies = ['setosa','versicolor','virginica'] #Guardamos los nombres de las especeis en una lista
for i in range(0,3):
    plt.scatter(X_pca[y==i,0],X_pca[y==i,1],label=especies[i]) #Las etiquetas las muestra por especies
plt.xlabel("Primer componente principal")
plt.ylabel("Segundo componente principal")
plt.title("PCA del conjunto Iris 2.0")
plt.legend() #Activamos la leyenda
plt.savefig("archivos_aparte/data_sns/PCA del conjunto Iris.png") #Guardamos el gráfico
plt.show()


