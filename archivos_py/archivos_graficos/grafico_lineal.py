import pandas as pd
import matplotlib.pyplot as plt #visualización de datos
import seaborn as sns #Gráficos estadísticos #importamos las librerías

df = pd.read_csv('archivos_aparte\\tareas.csv')
print(df) #leído correctamente
##sns.lineplot() lineal
sns.lineplot(x='fecha',y='tareas',data=df) #hacer el gráfico con las coordenadas, y el dataframe
plt.plot("01-06",6,'o') #Marcar un punto en el gráfico
plt.show() #Mostramos el gráfico
