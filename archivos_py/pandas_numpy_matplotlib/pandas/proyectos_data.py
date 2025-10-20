#Importamos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

array = np.arange(1,51)
array2 = [n*2 for n in array]
print(array)
print('-' * 50)
print("Valor total de los arrays:")
print(array.sum())
data = pd.DataFrame({'Producto': ['Manzana','Naranja','Plátano'],
                     'Precio': [10,8,12],
                     'Ventas': [30, 20,40]
                     })
print(f"Información de productos:\n{data}")
print('-' * 50)
print(f"Ganancia total de cada producto")
data['Ganancia'] = data['Precio'] * data['Ventas']
print(data)
print('-' * 50)
producto_mas_vendido = data.loc[data['Ganancia'].idxmax(),'Producto']
print(f"El producto más vendido es: {producto_mas_vendido}")
ventas_por_producto = data[['Producto','Ventas']]
print(ventas_por_producto)
precio_por_producto = data[['Producto','Precio']]
print(f"Precio por producto:")
print(precio_por_producto)

#HACER EL GRÁFICO
plt.bar(data["Producto"],data['Ventas'],color='skyblue')
plt.title("Ventas de productos")
plt.xlabel('Producto')
plt.ylabel('Precio')
plt.show()  #GRÁFICO DE PRODUCTOS Y PRECIOS

plt.plot(array,array2,color='red')
plt.title("Gráfico con arrays")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()  #GRÁFICO DE ARRAYS


#SUBGRÁFICOS
fig,(ax1,ax2) = plt.subplots(1,2)
ax1.plot(array,array2)
ax2.bar(data["Producto"],data['Ventas'])
plt.show()