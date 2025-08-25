#Importamos librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree
data = {"Clase": [1, 3, 2, 3, 1, 2, 3, 1, 2, 3],
    "Genero": [0, 0, 1, 1, 1, 0, 0, 1, 0, 1],  # 0 = Hombre, 1 = Mujer
    "Edad": [22, 35, 28, 8, 38, 40, 18, 55, 30, 4],
    "HermEsp": [1, 0, 0, 2, 1, 0, 0, 0, 1, 1],
    "PadHij": [0, 0, 0, 1, 0, 2, 0, 0, 1, 1],
    "Sobreviviente": [0, 0, 1, 1, 1, 0, 0, 1, 0, 1]}

df = pd.DataFrame(data)
print(df)
#Ver la distribución de sobrevivientes
sns.countplot(x='Sobreviviente',data=df,palette="coolwarm")
plt.title("Distribución de sobrevivientes")
plt.show()
#Entrenar un modelo de árbol de decisión
X = df.drop("Sobreviviente",axis=1)
y = df['Sobreviviente']
arbol = DecisionTreeClassifier(max_depth=4,random_state=42)
arbol.fit(X,y)
#Predicciones
pred_y = arbol.predict(X)
print(f"Precisión: {accuracy_score(y,pred_y)}")
#creamos una matriz de confusión
confusion = confusion_matrix(y,pred_y)
print(confusion)
#creamos un gráfico para lamatriz de confusión
disp = ConfusionMatrixDisplay(confusion_matrix=confusion)
disp.plot(values_format='.0f')  #Para quitar decimales
plt.show()
#Mostramos un arbol gráficamente
plt.figure(figsize=(10,8))
tree.plot_tree(arbol,filled=True,feature_names=X.columns)
plt.show()
#Graficamos la importancia de las variables
importancias = arbol.feature_importances_
columnas = X.columns
#creamos el gráfico
sns.barplot(x=columnas,y=importancias)
plt.title("Gráfico de importancias")
plt.show()
