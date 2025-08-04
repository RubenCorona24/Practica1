import pandas as pd
import matplotlib.pyplot as plt #visualización de datos
import seaborn as sns #Gráficos estadísticos #importamos las librerías
#Un gráfico de barras mediante la info. de el archivo fuente e ingresos
df = pd.read_csv('archivos_aparte\\ingresos.csv')

##sns.barplot() barras
sns.barplot(x='fuente',y='ingresos',data=df) #hacer el gráfico con las coordenadas, y el dataframe
total_ingresos = df['ingresos'].sum() #Obteniendo el total de ingresos
print(f"El total de ingresos es: {total_ingresos}USD") #Mostrar el total de ingresos
plt.show() #Mostramos el gráfico


