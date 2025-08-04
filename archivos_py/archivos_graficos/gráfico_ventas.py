#vAMOS A MOSTRAR MEDIANTE UN GRÁFICO LAS VENTAS DE UNA TIENDA --TOTAL 3 GRÁFICOS---
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt #importamos librerías

df = pd.read_csv('archivos_aparte\\ventas_tienda.csv') #Leer archivo
sns.barplot(x='día',y='ventas',data=df) #Hacer gráfico de barras
#Configuración de título y coordenadas
plt.title('Ventas por día de la semana')
plt.xlabel('Día')
plt.ylabel('Ventas ($)')
plt.show() #Mostrar el gráfico

#Otro Dataframe
data2 = {
    'día': ['Lunes', 'Lunes', 'Lunes', 'Martes', 'Martes', 'Martes', 
            'Miércoles', 'Miércoles', 'Miércoles'],
    'empleado': ['Ana', 'Luis', 'Sofía', 'Ana', 'Luis', 'Sofía', 'Ana', 'Luis', 'Sofía'],
    'tareas': [5, 7, 6, 8, 5, 9, 6, 7, 8],
    'departamento': ['Ventas', 'Marketing', 'Ventas', 'Ventas', 'Marketing', 'Ventas', 'Ventas', 'Marketing', 'Ventas']
}

df2 = pd.DataFrame(data2) #Hacer otro dataframe mediante información

#Gráfico de líneas de tareas completadas por empleado
sns.lineplot(x='día',y='tareas',hue='empleado',data=df2,marker='o')
plt.title('Tareas completadas por empleado')
plt.xlabel('Día')
plt.ylabel('Tareas')
plt.show()

#Gráfico de barras de comparación de tareas por departamento
sns.barplot(x='día',y='tareas',hue='departamento',data=df2)
plt.title('Comparación de tareas por departamento')
plt.show()

#'hue=' sirve para añadir una dimensión extra al gráfico, representa una categoría con diferentes colores