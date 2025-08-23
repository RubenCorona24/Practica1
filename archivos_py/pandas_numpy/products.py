#Crea un DataFrame con ventas de 6 productos diferentes(nombre,precio unitario,unidades vendidas)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox
p1 = np.random.randint(10,101)
vendidas_p1 =  np.random.randint(1,50)
p2 = np.random.randint(10,101)
vendidas_p2 =  np.random.randint(1,50)
p3 = np.random.randint(10,101)
vendidas_p3 =  np.random.randint(1,50)
p4 = np.random.randint(10,101)
vendidas_p4 =  np.random.randint(1,50)
p5 = np.random.randint(10,101)
vendidas_p5 =  np.random.randint(1,50)
p6 = np.random.randint(10,101)
vendidas_p6 =  np.random.randint(1,50) #Creamos los productos
names = pd.Series(['Papel Higiénico','Juguete','Monitor','Laptop','Ipad','Mouse'])
precios = pd.Series([p1,p2,p3,p4,p5,p6])
vendidos = pd.Series([vendidas_p1,vendidas_p2,vendidas_p3,vendidas_p4,vendidas_p5,vendidas_p6])
data_frame = pd.DataFrame({f'Producto':names,
                           'Precio': precios,
                           'Unidades vendidas':vendidos
                           })

#Calcula una columna de ingreso total (precio*unidades)
total = data_frame.iloc[:1,2].mean()
print(data_frame)
producto_mayor = data_frame.loc[data_frame['Precio'].idxmax(),'Producto']
promedio = data_frame['Precio'].mean()
promedio = promedio.round(2)
print(f"El promedio de precio en los productos es de: {promedio}")
print(f"El producto más caro: {producto_mayor}")
#Calcular el ingreso total
data_frame['Ingreso total'] = data_frame['Precio'] * data_frame['Unidades vendidas']

#Hacer el gráfico con Matplotlib  
plt.style.use('dark_background')
fig,(ax1,ax2) = plt.subplots(1,2)
ax1.plot(data_frame['Producto'],data_frame['Precio'],color='skyblue')
ax1.set(title='GRÁFICO LINEAL',xlabel='Productos',ylabel='Precios')
ax2.bar(data_frame['Producto'],data_frame['Precio'],color='skyblue')
ax2.set(title='Productos Mercado',xlabel='Productos',ylabel='Precios')
plt.show()

#Ahora con tkinter
import tkinter as tk
ventana = tk.Tk()
ventana.title("Ventas de Productos")
tk.Label(ventana,text='PRODUCTOS DEL MERCADO',foreground='green',font=("Arial",12,'bold')).pack(pady=15)
lbl_info = tk.Label(ventana,text=f'Info:\n{data_frame}',foreground='black',font=("Arial",10,'bold'))
lbl_info.pack(pady=15)
tk.Label(ventana,text=f'PRODUCTO MÁS VENDIDO:\n{producto_mayor}',foreground='black',font=("Arial",10,'bold')).pack(pady=15)
lbl_promedio = tk.Label(ventana)
lbl_promedio.pack(pady=20)
def ver_promedio():
    lbl_promedio.config(text=f"El promedio de costo de los productos: {promedio}(USD)",foreground='black',font=('Arial',12,'bold'))
tk.Button(ventana,text='PROMEDIO',command=ver_promedio,foreground='purple',font=('Arial',16,'bold')).pack(pady=20)
def ver_gráfico():
    fig, ax = plt.subplots()
    data_frame['Producto'] = data_frame['Producto'].astype(str)
    ax.bar(data_frame['Producto'],data_frame['Precio'],color='skyblue')
    ax.set(title='Productos Mercado',xlabel='Productos',ylabel='Precios')
    plt.show()
tk.Button(ventana,text='VISUALIZAR GRÁFICO',command=ver_gráfico,foreground='purple',font=('Arial',12,'bold')).pack(pady=20)
tk.Label(ventana,text='ESCRIBIR PRODUCTO',foreground='blue',font=('Arial',12,'bold')).pack(pady=15)
entrada = tk.Entry(ventana)
entrada.pack(pady=15)
def añadir_producto():
    if entrada.get():
        data_frame.loc[len(data_frame)] = {
    'Producto': entrada.get(),
    'Precio': 25.0
}
        lbl_info.config(text=f"Info:\n{data_frame}",foreground='black',font=('Arial',12,'bold'))
    else:
        messagebox.showerror("Error","Debes escribir un producto")

tk.Button(ventana,text='AÑADIR PRODUCTO',command=añadir_producto,foreground='purple',font=('Arial',12,'bold')).pack(pady=15)



    




ventana.geometry("1000x800")
ventana.mainloop()