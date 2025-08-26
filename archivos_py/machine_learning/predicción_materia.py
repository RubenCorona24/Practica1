#Crear un código para predecir si el estudiante aprobará o no mediante asistencias, notas, promedio
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree
import matplotlib.pyplot as plt
from random import *
a = []
for n in range(10):
    al = randint(1,100)
    a.append(al)
tareas = []
for n in range(10):
    t = randint(0,11)
    tareas.append(t)
aprobar = []
for n in range(10):
    num = choice([0,1])
    aprobar.append(num)
PromedioTareas = pd.Series(tareas)
asistencias  = pd.Series(a)
Aprobo = pd.Series(aprobar)


data = {'HorasEstudio': [2,10,5,7, 1, 3, 8, 6, 4, 9],
        'Asistencia': asistencias,
        'Tareas': PromedioTareas,
        'Aprobó': Aprobo}
df = pd.DataFrame(data)
print(df)
asistencia_maxima = df.loc[df['Asistencia'].idxmax(),'Asistencia']
print(f"El número máximo de asistencias fue de: {asistencia_maxima}")

#Hacer el gráfico
plt.style.use('dark_background')
fig,ax = plt.subplots()
ax.bar(df['Asistencia'],df['HorasEstudio'])
ax.set(title='GRÁFICA DE ASISTENCIAS Y HORAS DE ESTUDIO',xlabel='Asistencias',ylabel='Horas de estudio')
plt.show()

#Visualizar datos
sns.countplot(x="Aprobó", data=df, palette="coolwarm")
plt.title("Distribución de alumnos que aprobaron/reprobaron")
plt.show()  

#Entrenar modelo de arbol de decisión
X = df.drop("Aprobó",axis=1)
y = df['Aprobó']

arbol = DecisionTreeClassifier(max_depth=2,random_state=42)
arbol.fit(X,y)

#Predicciones
pred_y = arbol.predict(X)
print(f"Precisión: {accuracy_score(y,pred_y)}")

#Matriz de confusión
cm = confusion_matrix(y,pred_y)
ConfusionMatrixDisplay(confusion_matrix=cm).plot(values_format='.0f')
plt.show()

#Visualización del arbol
plt.figure(figsize=(10,8))
tree.plot_tree(arbol,feature_names=X.columns,class_names=["Reprobó","Aprobó"],filled=True)
plt.show()

#Importancia de las variables
importancias = arbol.feature_importances_
sns.barplot(x=X.columns,y=importancias,palette="viridis")
plt.title("Importancia de las variables en la predicción")
plt.show()