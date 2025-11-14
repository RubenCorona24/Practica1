#AGRUPAMIENTO DE PROMEDIOS K TIPO DE ALGORITMO DE MACHINE LEARNING APRENDIZAJE NO SUPERVISADO
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans #Modelo de kmeans
#importamos un dataset de seaborn "penguins"
pinguinos = sns.load_dataset("penguins")
#Visualizamos el dataset
print(pinguinos.head())
#Visualizamos los datos con un pairplot
plt.figure(figsize=(12,6))
#sns.pairplot(pinguinos)

#Trabajaremos con solo dos columnas para el modelo Kmeans
pinguinos.dropna(inplace=True)
pinguinos = pinguinos[['bill_length_mm','bill_depth_mm']]


#creamos el modelo kmeans
kmeans = KMeans(n_clusters=3,random_state=42) #n_clusters: definimos el número de grupos
kmeans.fit(pinguinos) #De argumento pasamos nuestro dataset


#Visualizamos los centroides y las etiquetas
centroides = kmeans.cluster_centers_
etiquetas = kmeans.labels_

#Visualizamos en un gráfico los centroides y las etiquetas
def grafico_kmeans():
    plt.figure(figsize=(12,6)) #Ajustamos el tamaño del gráfico
    #Scatterplot: de eje "X" pasamos el largo del pico, del eje "y" pasamos la profundidad del pico
    sns.scatterplot(data=pinguinos,x='bill_length_mm',y='bill_depth_mm',hue=etiquetas,palette='viridis')
    plt.scatter(centroides[:,0],centroides[:,1],c='red',s=100,label='Centroides',marker='x')
    plt.xlabel("Logintud del pico (milímetros)")
    plt.ylabel("Profundidad del pico (milímetros)")
    plt.title("K Means Clustering en el conjunto de Datos Pinguinos")    
    plt.legend() #Nos aseguramos que se muestren las etiquetas
    plt.savefig("archivos_aparte/data_sns/K Means Clustering pinguins") #Guardamos el archivo
    plt.show()
    
grafico_kmeans()

