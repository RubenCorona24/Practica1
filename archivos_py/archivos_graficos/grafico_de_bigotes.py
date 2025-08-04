#Haremos un gráfico de bigotes
import pandas as pd
import matplotlib.pyplot as plt #visualización de datos
import seaborn as sns #Gráficos estadísticos #importamos las librerías
#Un gráfico de barras mediante la info. de el archivo fuente e ingresos
df = pd.read_csv('archivos_aparte\\bigotes.csv')

##sns.boxplot()
sns.boxplot(x='categoría',y='valor',data=df) #hacer el gráfico de bigotes, y el dataframe
plt.show() #Mostramos el gráfico
