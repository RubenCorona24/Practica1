#Project day 14 -------anonymization and pseudonymization---------
#Importar librerías 
import pandas as pd
import numpy as np
import uuid #Para pseudonimización
from sklearn.utils import resample #Para remuestreo

#Leemos el dataframe
df = pd.read_csv(r"C:\Users\coron\Downloads\clientes.csv")

def info_df():
    print(f"Primeras 10 filas:\n{df.head()}\n")
    print(f"Últimas 10 filas:\n{df.tail()}")
    print(df.describe)
    print(df.info)
    print(df.memory_usage(deep=True)) #Visualizamos la memoria usada del df
    print(f"Valores nulos:\n{df.isnull().sum()}")

def anonimizar_df():
    #Eliminamos las columnas innecesarias
    df.drop('direccion',axis=1,inplace=True)
    #Aplicamos redondeo a edad
    df['edad'] = (df['edad']//10) *10
    #Aplicamos ruido
    df['salario'] = df['salario']+np.random.normal(0,100,size=len(df))
    return df #Nos devuelve df anonimizado

df = anonimizar_df()

tokens = {} #Creamos diccionario vacio para tokens
#Función para tokenizar dato
def tokenizar(dato):
    token = str(uuid.uuid4())
    tokens[token] = dato
    return token
#Función para recuperar dato
def recuperar_dato(token):
    return tokens.get(token,'Token No Válido')

#Pseudinimizamos los datos (nombre)
def pseudonimizar_df():
    df['nombre']= df['nombre'].apply(tokenizar)
    return df
df = pseudonimizar_df()

#Balanceamos los datos por agrupamiento(groupby) y remuestreo(resample)
def balancear_datos():
    agrupado = df.groupby('categoria')
    df_balanceado = pd.DataFrame()
    for nombre,grupo in agrupado:
        df_balanceado = pd.concat([df_balanceado,resample(grupo,replace=True,n_samples=1000,random_state=42)])
    return df_balanceado #Devolvemos el df balanceado
df = balancear_datos()
print(f"DataFrame anonimizado, pseudonimizado y balanceado mediante remuestreo:\n{df}")

#Visualizamos los datos 
import matplotlib.pyplot as plt
import seaborn as sns
#Visualización de relación de Categoría con Salario
plt.bar(df['categoria'].unique(),df.groupby('categoria')['salario'].mean())
plt.xlabel("Categoría")
plt.ylabel("Salario Promedio")
plt.title("Salario Promedio por categoría")
plt.show()

#Visualización de distribución de edades por densidad
plt.figure(figsize=(12,7))
sns.histplot(df['edad'],kde=True,color='skyblue',bins=30)
plt.title("Distribución de edades de los clientes con Curva de Densidad")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

#Mapa de calor de correlación entre variables
plt.figure(figsize=(10,8))
#Calculamos matriz de correlación
correlation_matrix = df[['edad','salario','categoria']].corr()
heatmap = sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm')
heatmap.set(title='Mapa de Calor de Correlación entre Variables')
plt.show()