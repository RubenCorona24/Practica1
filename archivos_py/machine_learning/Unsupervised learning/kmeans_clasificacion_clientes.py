#REALIZAMOS UNA CLASIFICACIÓN DE CLIENTES CON AYUDA DEL ALGORITMO KMEANS DE MACHINE LEARNING
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#cargamos el dataset de clientes
df = pd.read_csv("archivos_aparte/archivos_csv/datos_clientes.csv")
print(df.head()) #Leemos primeras columnas

def verificar_data(df):
    nulos = df.isnull().sum()
    print(f"Valores nulos: {nulos}")
    print(df.describe)
    print(df.info)
    new_data = df.dropna()
    return new_data

df = verificar_data(df)

def graficar_datos():
    plt.figure(figsize=(10,6))
    plt.scatter(df['edad'],df['tiempo_promedio_min'],marker='o',label='Tiempo promedio')
    plt.xlabel("Edad")
    plt.ylabel("Tiempo Promedio Minutos")
    plt.title("RELACIÓN EDAD/TIEMPO MIN EN USUARIOS DE SUPERMERCADO")
    plt.scatter(df['frecuencia_visitas'],df['tiempo_promedio_min'],marker='x',label='Frecuencia de visitas')
    plt.legend()
    plt.show()
    #Otro gráfico
    plt.scatter(df['edad'],df['frecuencia_visitas'],marker='o',c='green')
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia de Visitas (X semana)")
    plt.title("Relación edad con frecuencia de visitas")
    plt.show()
    #tercer gráfico
    plt.scatter(df['edad'],df['gasto_anual'],marker='o',c='red')
    plt.xlabel("Edad")
    plt.ylabel("Gasto anual MXM")
    plt.title("Relación edad con gasto anual")
    plt.show()


graficar_datos() #Con el primer gráfico observamos que los usuarios con edad entre 40 y 50 años tienden a pasar mayor tiempo en el supermercado
#Se observa gráficamente que las personas de mayor edad visitan con mayor frecuencia el supermercado.

#Normalizamos los datos
data = df[['frecuencia_visitas','gasto_anual']]


#Creamos el modelo
kmeans = KMeans(n_clusters=3,random_state=42)
kmeans.fit(data) #Entrenamos al modelo

#Obtenemos las etiquetas y los centroides
centroides = kmeans.cluster_centers_
etiquetas = kmeans.labels_

#Graficamos los datos
sns.scatterplot(data=df,x='frecuencia_visitas',y='gasto_anual',hue=etiquetas,palette='viridis')
plt.scatter(centroides[:,0],centroides[:,1],c='red',s=200,marker='x',label=centroides)
plt.title("Modelo KMeans con datos de usuarios en Mercado")
plt.show()