#Clustering jerárquico
#El clustering jerárquico es un algoritmo de aprendizaje automático no supervisado que agrupa datos en una estructura de árbol anidado (o jerarquía)
# basándose en su similitud. Comienza con cada punto de datos en su propio clúster y luego fusiona los clústeres más cercanos sucesivamente
# (método aglomerativo) hasta que todos los datos están en un solo grupo. El resultado es una visualización llamada dendrograma,
# que representa la jerarquía de grupos y permite identificar cómo se agrupan los datos.

#Importamos librerías
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

#Cargamos el dataset
iris = load_iris()
#Dividimos la variable independiente, en este caso iris.data
X = iris.data
#Construimos el clustering jerárquico con linkage()
z = linkage(X,method='ward') #Utilizamos el método ward: minimiza la variedad dentro de los clusters
#dibujamos el dendrograma
plt.figure(figsize=(12,6))
dendrogram(z,orientation='top',labels=iris.target,distance_sort='descending',show_leaf_counts=True)
plt.title("Dendrograma del Clustering Jerárquico de Iris")
plt.xlabel("Muestras")
plt.ylabel("Distancia")
plt.show() #Mostramos

#Obtener los clusters finales
clusters = fcluster(z,t=3,criterion='maxclust')
#z: resultado del linkage
#t: número de clusters
#criterion: agrupa en t clusters

#Visualización de los clusters
plt.scatter(X[:,0], X[:,1], c=clusters)
plt.title("Clusters Jerárquicos de Iris")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.show()
#
