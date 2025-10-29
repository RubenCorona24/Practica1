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


#creamos un gráfico relplot (gráfico de relación)
try:
    g = sns.relplot(data=df,x='Eje x',y='Eje y',kind='line')
    plt.show()
except:
    print("ERROR")