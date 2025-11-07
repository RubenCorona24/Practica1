import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Datos
data = {'Horas': [1, 2, 3, 4, 5, 6],
        'Aprobó': [0, 0, 0, 1, 1, 1]}
df = pd.DataFrame(data)

# Variables
X = df[['Horas']]
y = df['Aprobó']

# Modelo
modelo = LogisticRegression()
modelo.fit(X, y)

# Predicción para un nuevo valor
nuevas_horas = [[3.5]]
prob = modelo.predict_proba(nuevas_horas)
print(f"Probabilidad de aprobar estudiando 3.5 horas: {prob[0][1]*100:.2f}%")

# Visualización
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, modelo.predict_proba(X)[:, 1], color='red', label='Probabilidad de aprobar')
plt.title('Regresión Logística: Aprobado vs Horas de Estudio')
plt.xlabel('Horas de estudio')
plt.ylabel('Probabilidad de aprobar')
plt.grid(True)
plt.legend()
plt.show()

#OTRO EJEMPLO DE REGRESION LOGISTICA
df2 = pd.DataFrame({
    'Edad': [25, 30, 35, 40, 45, 50, 55, 60],
    'Presion_Arterial': [120, 125, 130, 140, 145, 150, 160, 165],
    'Glucosa': [80, 90, 100, 110, 120, 130, 140, 150],
    'Enfermo': [0, 0, 0, 1, 1, 1, 1, 1]
})

#Separamos las variables
X2 = df2[['Edad','Presion_Arterial','Glucosa']]
y2 = df2['Enfermo']

#Dividir en entrenamiento y prueba
X_entrena,X_prueba,y_entrena,y_prueba = train_test_split(X2,y2,train_size=0.8)
#Crear y entrenar el modelo
model2 = LogisticRegression()
model2.fit(X_entrena,y_entrena  )
#Evaluar el modelo
score = model2.score(X_prueba,y_prueba)
print(f"Precisión del modelo: {score*100:.2f}%")
#Probamos el modelo con paciente de 45 años, presion 145 y glucosa de 125
nuevo_paciente = [[45,145,125]]
prediccion = model2.predict(nuevo_paciente)
print(f"Diagnóstico del paciente: {'Enfermo' if prediccion[0]==1 else 'Sano'}")