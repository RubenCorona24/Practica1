#VAMOS A REALIZAR GRÁFICOS CON MATPLOTLIB Y PANDAS
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("archivos_aparte\\ventas_tienda.csv") #Leemos el archivo csv

df.plot(x="día", y="ventas", kind="bar", color="skyblue")

plt.title("Ventas Semanales")
plt.xlabel("Producto")
plt.ylabel("Cantidad vendida")
plt.show()

