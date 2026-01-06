#------------PROYECTO DE ML CON HEART------------

#Importamos librerías
import pandas as pd #Análisis de datos
from sklearn.model_selection import train_test_split #División en entrenamiento/prueba
from sklearn.preprocessing import StandardScaler #Transformador
from sklearn.neighbors import KNeighborsClassifier #Modelo
from sklearn.pipeline import make_pipeline #Pipeline (procesos conectados)
import matplotlib.pyplot as plt #Visualizaciones

df = pd.read_csv(r"C:\Users\coron\Downloads\heart.csv")
try:
    print(df.head(5))
except FileNotFoundError:
    print("No se encontró el archivo")
except Exception as e:
    print(f"Error {e}")

def description():
    print(df.describe)
    print(df.info)
    print(f"Valores nulos: {df.isnull().sum()}")

#Graficamos campos con matplotlibx  
def graficar():
    fig,axs = plt.subplots(1,2)
    axs[0].scatter(df['trtbps'],df['age'],s=100,marker='x',color='green')
    axs[0].set_title("Relación entre edad y presión arterial")
    axs[0].set_ylabel("Edad")
    axs[0].set_xlabel("Presión arterial")
    axs[1].hist(df['thalachh'],color='red')
    axs[1].set_title("Distribución entre frecuencia cardiaca")
    axs[1].set_ylabel("Frecuencia cardiaca")
    axs[1].set_xlabel("Frecuencia")
    plt.tight_layout()
    plt.show() #Mostramos los gráficos
try:
    graficar()
except Exception as e:
    print(f"Error {e}")

#EMPEZAMOS CON EL ENTRENAMIENTO DEL ALGORITMO DE K NEIGHBORS UTILIZANDO PIPELINE
#Dividimos variables (predictorias y objetivo)
X = df.drop("output",axis=1)
y = df['output']

#Dividimos en entrenamiento y prueba con train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

#Creación del pipeline que incluye al transformador y estimador
pipeline = make_pipeline(StandardScaler(),KNeighborsClassifier())

#Entrenamos al pipeline que incluye escalamiento de datos y entrenamiento del modelo
pipeline.fit(X_train,y_train)

#Evaluación del modelo utilizando score
score= pipeline.score(X_test,y_test)
predicciones = pipeline.predict(X_test)
print(f"Precisión del modelo:{score:.2f}")
print(f"Predicciones del modelo:{predicciones[:10]}")

#Predicción con un nuevo paciente (CASO REAL)
patient = [[63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]]
result = pipeline.predict(patient)
if result[0] == 1:
    print("RIESGO DE ENFERMEDAD CARDIACA")
else:
    print("PACIENTE EN BUENAS CONDICIONES")