import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = sns.load_dataset("penguins")
#Cambiar el estilo del gráfico
sns.set_theme(style='dark')
g = sns.barplot(data=data,x='species',y='body_mass_g',hue='sex')
g.set_title("Relación especies/masa en gramos")
g.set_xlabel("Especies")
g.set_ylabel("Masa gramos")
plt.show() #Mostramos el gráfico