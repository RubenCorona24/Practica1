import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = sns.load_dataset("penguins")
#Cambiar el estilo del gráfico
def llamar_gráfico():
    sns.set_theme(style='dark')
    g = sns.barplot(data=data,x='species',y='body_mass_g',hue='sex')
    g.set_title("Relación especies/masa en gramos")
    g.set_xlabel("Especies")
    g.set_ylabel("Masa gramos")
    plt.show() #Mostramos el gráfico

#-------VAMOS A UTILIZAR OTRO DATAFRAME DE PANDAS-------
df = pd.read_csv("archivos_aparte/Datos_Ventas_Tienda.csv")
print(df)
g = sns.barplot(data=df,x='Producto',y='Total Venta')
g.set_title("Productos y Ventas")
g.set_xlabel("Productos")
g.set_ylabel("Ventas totales")
plt.xticks(rotation=45)
plt.show()
#Por lo que vemos en la gráfica más personas compran la parte de productos electrónicos

#Filtrar valores para hue
values = []
for n in df['Total Venta']:
    if n >=1000:
        data = "Éxito"
    else:
        data = "Fracaso"
    values.append(data)
df['Demanda'] = values
#----NUEVO DATAFRAME CON COLUMNA DE DEMANDA----
def g2():
    g2= sns.barplot(data=df,x='Producto',y='Total Venta',hue='Demanda')
    g2.set_title("Productos y Ventas")
    g2.set_xlabel("Productos")
    g2.set_ylabel("Ventas totales")
    plt.xticks(rotation=45)
    plt.show()

def g3():
    g3 = sns.barplot(data=df,x='Cantidad',y='Precio Unitario',hue='Producto')
    g3.set_title("Cantidad y Precio")
    g3.set_ylabel("Precio Unitario")
    g3.set_xlabel("Cantidad")
    plt.xticks(rotation=40)
    plt.savefig("archivos_aparte/Distribución Precio Unitario_Cantidad")
    plt.show()
g3()