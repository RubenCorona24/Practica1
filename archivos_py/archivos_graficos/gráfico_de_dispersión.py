#Vamos a mostrar un gráfico de dispersión
import pandas as pd
import matplotlib.pyplot as plt #visualización de datos
import seaborn as sns #Gráficos estadísticos #importamos las librerías
#Un gráfico de barras mediante la info. de el archivo fuente e ingresos
df = pd.read_csv('archivos_aparte\\dispersion.csv')


sns.scatterplot(x='tiempo',y='dinero',data=df) #hacer el gráfico de dispersión, y el dataframe
plt.show() #Mostramos el gráfico
