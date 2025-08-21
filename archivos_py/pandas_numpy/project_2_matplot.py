import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("archivos_aparte\\productos.csv") #Leemos archivo
print(df.head(4))
df2 = pd.read_csv("archivos_aparte\\tareas.csv")
print("Tareas de la semana:")
print(df2.head(2))

plt.style.use("dark_background") #Cambiamos el estilo
fig,(ax1,ax2) = plt.subplots(1,2)
ax1.bar(df['Mes'],df['Ventas'],color='red')
ax1.set(title='Ventas anuales',xlabel='Mes',ylabel='Ventas (USD)')
ax2.bar(df2['fecha'],df2['tareas'],color='blue')
ax2.set(title='TAREAS SEMANALES',xlabel='Fecha',ylabel='Tareas')
plt.show() #Mostramos las gráficas

array = np.arange(1,101)
array2 = array*2

lista = [10,20,30,40,50,60,70]
lista2 = [n*2 for n in lista]

df3 = pd.read_csv("archivos_aparte\\ingresos.csv")
lista3 = [5,10,20,40,80,160]
lista4 = [n*2 for n in lista3]
#AHORA UNA FIGURA CON 4 GRÁFICOS
fig,((ax3,ax4),(ax5,ax6)) = plt.subplots(2,2)
ax3.plot(array,array2,color='purple')
ax3.set(title='GRÁFICA CON ARRAYS',xlabel='Array 1',ylabel='Array2')
ax4.plot(lista,lista2,color='orange')
ax4.set(title='GRÁFICA CON LISTAS')
ax5.bar(df3['fuente'],df3['ingresos'],color='red')
ax5.set(title='INGRESOS POR OCUPACIÓN',xlabel='FUentes',ylabel='Ingresos')
ax6.plot(lista3,lista4,color='blue')
ax6.set(title='GRÁFICA LINEAL',xlabel='Eje x',ylabel='Eje y')
plt.show()

df4 = pd.read_csv("archivos_aparte\\comida_rápida.csv")
suma_ventas = df['Ventas'].sum()
producto_mejor = df4.loc[df4['Ventas'].idxmax(),'Comida']
import tkinter as tk
ventana = tk.Tk()
lbl_productos = tk.Label(text=f'PRODCUCTOS Y VENTAS:\n {df4}',foreground='black',font=('Arial',12,'bold'))
lbl_productos.pack(pady=10)
lbl_ventas = tk.Label()
lbl_ventas.pack()
def ver_ventas():
 lbl_ventas.config(text=f'Las ventas totales fueron: {suma_ventas}USD',foreground='red',font=('Arial',12,'bold')).pack(pady=15)
def ver_pruducto():
 lbl_producto.config(text=f"El producto más vendido: {producto_mejor}",foreground='green',font=('Arial',12,'bold'))
    
lbl_producto = tk.Label()
lbl_producto.pack()
tk.Button(text='PRODUCTO MÁS VENDIDO',command=ver_pruducto,foreground='purple',font=('Arial',12,'bold')).pack(pady=15)

tk.Button(text='VER VENTAS TOTALES', command=ver_ventas,foreground='purple',font=('Arial',16,'bold')).pack(pady=15)
def mostrar_gráfica():
 fig,ax = plt.subplots()
 ax.bar(df4['Comida'],df4['Ventas'],color='skyblue')
 ax.set(title='VENTAS RESTAURANTE "GLOSARIO"',xlabel='Comidas',ylabel='Ventas')
 plt.show()
tk.Button(text='MOSTRAR GRÁFICO',command=mostrar_gráfica,foreground='purple',font=('Arial',16,'bold')).pack(pady=15)
def cerrar():
 ventana.destroy()
tk.Button(text='CERRAR',command=cerrar,foreground='purple',font=('Arial',16,'bold')).pack(pady=15)
 
ventana.mainloop()
