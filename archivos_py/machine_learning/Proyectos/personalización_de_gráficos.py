#Proyecto personal de visualización de datos con plotly
#--ANÁLISIS DE HORAS DE SUEÑO----
import pandas as pd #Para manejar datos
import numpy as np #Para operaciones
import matplotlib.pyplot as plt #Visualizaciones
from sklearn.model_selection import cross_val_score,train_test_split
from sklearn.ensemble import RandomForestRegressor #Modelo 
from sklearn.preprocessing import StandardScaler #Preprocesamiento con StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
df = pd.read_csv("archivos_aparte/dataset_sleep.csv")
from functions import visualize
visualize(df)

#Reemplazar el signo "?" con un np.nan
df.replace("?",np.nan,inplace=True)
df = df.dropna()
df.columns = df.columns.str.strip()

#Reemplazamos columnas por datos tipo numérico
for col in df:
    df[col] = pd.to_numeric(df[col], errors="coerce")
print(df.dtypes) #Confirmamos tipos de datos

#Hacemos visualizaciones generales del dataset
plt.plot(df['body_weight'],df['total_sleep'])
plt.title("Relación entre peso en kg y total de sueño hr")
plt.xlabel("Peso (kg)")
plt.ylabel("Horas de sueño")
plt.show()

#Gráfico de barras de tiempo de gestación y horas de sueño
plt.bar(df['gestation_time'],df['total_sleep'])
plt.title("Relación entre tiempo de gestación y horas de sueño")
plt.xlabel("Tiempo gestación")
plt.ylabel("Horas de sueño")
plt.show()

#Dividimos variables independientes y dependientes
X = df[['gestation_time', 'sleep_exposure_index', 'danger_index']]
X = X.fillna(X.mean())
y = df['total_sleep']  
y = y.fillna(y.mean())

#Creamos el modelo
model = RandomForestRegressor(n_estimators=800,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42)

#Validación cruzada
score = cross_val_score(model,X,y,cv=5)
print(f"Score de validación cruzada: {score.mean():.2f}")

#Entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model.fit(X_train,y_train)
y_pred = model.predict(X_test) #Predecimos datos

print(f"R2 score: {r2_score(y_test,y_pred)}")
print(f"MAE: {mean_absolute_error(y_test,y_pred)}")
print(f"MSE: {mean_squared_error(y_test,y_pred)}")

print(f"Predicciones del modelo: {y_pred}")
print(f"Datos reales: {y_test}")
print(f"Score del modelo {model.score(X_test,y_test):.2f}")

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

importances = pd.Series(model.feature_importances_,index=X.columns)
importances = importances.sort_values(ascending=False)

importances.plot(kind='bar')
plt.title("Importancia de las variables")
plt.show()
