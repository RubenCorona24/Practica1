#Análisis y clasificación de clientes

import pandas as pd #Manipulación y lectura de datos
import  numpy as np #Trabajar numéricamente
import seaborn as sns #Visualización de datos
import matplotlib.pyplot as plt #Visualización de datos
from sklearn.model_selection import train_test_split #Dividir entrenamiento/prueba
from sklearn.preprocessing import MinMaxScaler #Para escalar datos
from sklearn.cluster import KMeans
from sklearn.decomposition import  PCA
from scipy.cluster.hierarchy import dendrogram,linkage
from tkinter import messagebox
#Leemos el archuvo csv
df = pd.read_csv(r"C:\Users\coron\OneDrive\Escritorio\Algoritmia\archivos_aparte\archivos_csv\customer_data.csv")
print(df.head(5)) #Imprimimos las primeras 5 filas del df
def limpieza_datos():
    nulos = df.isnull().sum()
    print(f"Valores nulos:\n{nulos}\n")
    print(f'Información:\n{df.info}\n')
    print(df.describe)
    limpio = df.dropna()
    return limpio
df = limpieza_datos() #Reescribimos el df limpio sin valores nulos

#Escalamos los datos utilizando MinMaxScaler
scaler = MinMaxScaler()
df_escalado = scaler.fit_transform(df[['Edad','Ingresos Anuales (k$)','Puntuación de Gasto (1-100)']])

#Reducción de componentes utilizando PCA
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_escalado) #Transformamos el df escalado en df pca

#Clustering: Kmeans y clustering paara agrupar datos
kmeans = KMeans(n_clusters=3,random_state=42) #No. de clusters: 2
kmeans.fit(df_pca) #Entrenamos el modelo
kmeans_clsuters = kmeans.fit_predict(df_escalado)
centroids = kmeans.cluster_centers_ #Extraemos los centroides
labels = kmeans.labels_ #Extraemos las etiquetas


#Preparamos el clustering Jerárquico on linkage
Z = linkage(df_pca,method='ward') #Método ward para minimizar la varianza dentro de los clusters

#SVD: descomposición de singular value
U,sigma,Vt = np.linalg.svd(df_escalado)


#Visualización de los datos
def estadisticas():
    plt.figure(figsize=(12,6)) #Configuramos la figura
    sns.barplot(x=df['Categoría de Producto Favorito'],y=df['Edad'],hue=df['Categoría de Producto Favorito'],fill=True)
    plt.title("Estadísticas de Edad/Categoría de Producto Favorito")
    plt.xlabel("Categoría de Producto Favorito")
    plt.ylabel("Edad")
    plt.show() #Mostramos el gráfico
    #Realizamos otro gráfico
    sns.scatterplot(x=df['Edad'],y=df['Puntuación de Gasto (1-100)'])
    plt.title("Estadísticas de Puntuación de Gasto/Edad de Producto Favorito")
    plt.xlabel("Edad")
    plt.ylabel("Puntuación de Gasto (1-100")
    plt.show()

#Visualización de PCA (componentes principales)
def grafico_pca():
    plt.figure(figsize=(12,6))
    sns.scatterplot(x=df_pca[:,0],y=df_pca[:,1],hue=kmeans_clsuters,palette='viridis')
    plt.scatter(centroids[:,0],centroids[:,1],marker='x',c='red',s=200,label='Centroids') #Marcamos los centroides
    plt.title("Componentes principales (PCA) de clientes")
    plt.xlabel("Componente principal 1")
    plt.ylabel("Componente principal 2")
    plt.legend(title='Clusters') #Activamos la leyenda
    plt.grid(True) #Activamos las casillas
    plt.show()

def kmeans_graph():
    plt.figure(figsize=(12,6))
    plt.scatter(df_pca[:,0],df_pca[:,1],c=labels,cmap='rainbow')
    plt.scatter(centroids[:,0],centroids[:,1],c='red',marker='x',label='Centroides',s=200)
    plt.title("Agrupamiento de promedios K de clientes")
    plt.xlabel("Primer componente principal")
    plt.ylabel("Segundo componente principal")
    plt.legend()
    plt.show()

#Visualizamos el dendrograma (Clustering Jerárquico)
def hierarchical_clustering():
    plt.figure(figsize=(12,6))
    dendrogram(Z,orientation='top',distance_sort='descending',show_leaf_counts=True)
    plt.title("Dendrograma de Clustering Jerárquico de Clientes")
    plt.xlabel("Muestras")
    plt.ylabel("Distamcias")
    plt.show() #Mostramos el dendrograma

def menu():
    while True:
        print("-------BIENVENIDO AL MENÚ DE CLASIFICACIÓN DE CLIENTEES---------")
        print("Tienes 4 opciones para visualuización de datos:\n1: Ver estadísticas generales\n2:Visuañizar componentes principales de PCA\n3: Visualizar los centroides y los componentes principales de KMeans\n4: Visualizar el dendrograma del Clustering Jerárquico\n5: Ver los primeros y últimos 10 filas del DataFrame\n6: Salir del programa ")
        elige = int(input("Elige tu opción: "))
        if elige == 1:
            print("Opción de Ver Estadísticas generales")
            estadisticas()
            continue
        elif elige ==2:
            print("Opción de ver componentes PCA")
            grafico_pca()
            continue
        elif elige ==3:
            print("Opción de ver centroides y KMeans clustering")
            kmeans_graph()
            continue
        elif elige == 4:
            print("Opción de ver dendrograma del clustering Jerárquico")
            hierarchical_clustering()
            continue
        elif elige == 5:
            print("Opción de ver DataFrame")
            print(f"Primeras 10 Filas:\n{df.head()}\nÚltimas 10 filas:\n{df.tail()}")
            continue
        elif elige==6:
            print("Fue un gusto ayudarte!!")
            break
        else:
             messagebox.showerror("ERRORX","Solo puedes seleccionar: 1,2,3,4,5") #Mostramos error en pantalla
             continue
menu()
