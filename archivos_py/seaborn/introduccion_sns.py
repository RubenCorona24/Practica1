#Seaborn es una librería basada en matplotlib (crea gráficos estadísticos)
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Creamos dos variables 
x = [122,444,555,666,777,888]
y = np.sqrt(x)
df = pd.DataFrame({'Eje x': x,
                  'Eje y':y})

#Creamos datos ideales para un displot (distribución)
df2 = pd.DataFrame({
    'Edades': [13,22,21,23,66,74],
    'Salary': [1200,3400,3600,3700,1100,6600],
    'Nombres': ['Gerardo','Arturo','Celeste','Juan','Adolfo','Leonidas']
})

#Creamos datos ideales para un displot(categórica)
df3 = pd.DataFrame({
    'Fumadores': [True,False,False,True,True],
    'Ages': [18,34,77,12,14],
    'Nombres': ['Elizabeth','Armando','Spencer','Nath','Eidan']
})
#Filtro para mayores de edad
filtro = df3['Ages'] >=18
filtrado = df3[filtro]
values = []
for n in df3['Ages']:
    if n <18:
        data = "No puede tomar"
    else:
        data = "Si puede tomar(no recomendable)"
    values.append(data)
df3['Puede tomar'] = values
print(df3)
    #creamos un gráfico relplot (gráfico de relación)
g = sns.lineplot(data=df,x='Eje x',y='Eje y')
g.set_title("Relación entre los ejes x/y")
plt.show()
#Ahora creamos una figura de tipo displot (distribución)
g2 = sns.histplot(data=df2,x='Salary')
g2.set_title("Distribución de salarios entre empleados")
plt.show()
#Ahora creamos una figura tipo barplot(en categórica)
g3 = sns.barplot(data=df3,x='Nombres',y='Ages',hue='Puede tomar')
g3.set_title("Datos de Licencia de Bebidas")
#hue: marca de diferente color dependiendo de la categoría
plt.show()