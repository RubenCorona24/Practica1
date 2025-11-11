#PROYECTO DÍA 11
#Librerias para visualización
import matplotlib.pyplot as plt
#Librería para cargar DataFrames
import pandas as pd
#Librerías para modelos
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.ensemble import  RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#Leer el dataframe
df = pd.read_csv("archivos_aparte/archivos_csv/Ventas (1).csv")
print(df.head(5))

#Mostrar información del df
def info_df(data):
    df.describe()
    df.info()
    nulos = df.isnull().sum()
    print(nulos)

#Creamos una escala con MinMaxScaler
escala = MinMaxScaler() 
columnas_escalar = df.drop(['Ventas','Fecha'],axis=1).columns #las columnas a escalar
normado = escala.fit_transform(df[columnas_escalar]) #hacer un normado con método escala.fit_transform
df_normado = pd.DataFrame(normado) #convertir el normado en un df
df_normado['Ventas'] = df['Ventas']
print(df_normado.head()) #Visualizamos las primeras filas del df normado
#Graficar la información del DataFrame conforme a los datos
def graficar(data):
    plt.bar(data['DíaDeLaSemana'],data['Ventas'])
    plt.title("RELACIÓN ENTRE DÍAS DE LA SEMANA Y VENTAS")
    plt.xlabel("Días de la Semana")
    plt.ylabel("Ventas Totales")
    plt.show() #Mostramos la figura

    #Otra figura para visualizar los festivos y promociones
    plt.scatter(data['Promociones'],data['Ventas'])
    plt.title("RELACIÓN ENTRE PROMOCIONES Y VENTAS")
    plt.xlabel("Promociones (si/no)")
    plt.ylabel("Ventas")
    plt.show()
graficar(df)

#SEPARAR LAS VARIABLES INDEPENDIENTES DE LAS DEPENDIENTES (X,Y)
X = df_normado.drop('Ventas',axis=1) #Siempre poner axis=1
y = df_normado['Ventas']

#DIVIDIR EN ENTRENAMIENTO Y PRUEBA CON TRAIN_TEST_SPLIT()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.8,random_state=42)
modelos = [
    ('Regresión Lineal', LinearRegression()),
    ('Árbol de decisión', DecisionTreeClassifier()),
    ('Bosques aleatorios', RandomForestRegressor())
]
#EVALUAMOS EL SCORE DE CADA MODELO Y MEDIANTE ELLO ELEGIMOS UNO
for name,modelo in modelos:
    modelo.fit(X_train,y_train) #Entrenamos a cada modelo
    score= modelo.score(X_test,y_test)
    print(f"{name}: {score:.5f}")
    
#COMO RESULTADO TRABAJAREMOS CON REGRESIÓN LINEAL

modelo_lineal = DecisionTreeClassifier()
modelo_lineal.fit(X_train,y_train) #Entrenamos al modelo
predicciones_lineal = modelo_lineal.predict(X_test)
print(f"Predicciones del modelo: {predicciones_lineal}")

#Graficamos el modelo lineal
def graf_modelo():
    plt.figure(figsize=(12,6))
    plt.scatter(y_test,predicciones_lineal,alpha=0.5) #alpha: indica el nivel de transparencia
    plt.plot([y.min(),y.max()],[y.min(),y.max()]) #hacemos un plot (línea)
    #Ponemos las etiquetas y mostramos el gráfico
    plt.xlabel("Ventas reales")
    plt.ylabel("Ventas predichas")
    plt.title("Ventas Reales vs Ventas Predichas")
    plt.show()
graf_modelo()

df_test = pd.DataFrame({'Real':y_test,'Prediccion':predicciones_lineal})
df_test= df_test.sort_index()
#Graficamos las ventas reales vs ventas predichas a lo largo del tiempo
def graph_modelo2():
    plt.figure(figsize=(12,6))
    plt.plot(df_test['Real'],label='Ventas Reales',alpha=0.7)
    plt.plot(df_test['Prediccion'],label='Ventas predichas',alpha=0.7)
    plt.legend() #Activamos la leyenda
    plt.title("Comparación ventas reales y ventas predichas a lo largo del tiempo")
    plt.savefig('archivos_aparte/data_sns/Ventas reales y ventas predichas.png') #Guardamos el gráfico
    plt.show()

graph_modelo2()

    



