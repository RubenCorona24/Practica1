import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk


df = pd.read_csv("archivos_aparte\\review.csv")

mas_alto = df.loc[df['Ganancias'].idxmax(),'Nombre']
ventana = tk.Tk()
ventana.title("Resultados de las ganancias anuales")
ventana.geometry("900x600")
tk.Label(ventana,text="RESULTADOS DE LAS GANANCIAS ANUALES",foreground='green',font=('Arial',12,'bold')).pack(pady=15)
lbl_resultados= tk.Label(ventana)
lbl_resultados.pack(pady=15)
lbl_primeros = tk.Label(ventana)
lbl_primeros.pack(pady=15)
def mostrar_resultado():
    lbl_resultados.config(text=df,foreground='black',font=('Arial',12,'bold'))
tk.Button(ventana,text='Mostrar Resultados Completo',command=mostrar_resultado,foreground='red',font=('Arial',12,'bold')).pack(pady=15)
def mostrar_primeros():
    top_primeros = df.sort_values(by='Ganancias',ascending=False).head(3)
    lbl_primeros.config(text=f"Primeros tres lugares:\n{top_primeros}",foreground='black',font=("Arial",10,'bold'))
tk.Button(ventana,text='Mostrar primeros 3 lugares',command=mostrar_primeros,foreground='red',font=('Arial',12,'bold')).pack(pady=15)
lbl_ultimos = tk.Label(ventana)
lbl_ultimos.pack(pady=15)
def mostrar_ultimos_lugares():
    top_ultimos = df.sort_values(by='Ganancias',ascending=True).head(3)
    lbl_ultimos.config(text=f"Los últimos lugares en ventas:\n{top_ultimos}",foreground='black',font=('Arial',10,'bold'))
tk.Button(ventana,text='Mostrar últimos 3 lugares',command=mostrar_ultimos_lugares,foreground='red',font=('Arial',12,'bold')).pack(pady=15)
def cerrar():
    ventana.destroy()
tk.Button(ventana,text='SALIR',command=cerrar,foreground='red',font=('Arial',12,'bold')).pack(pady=15)
def reiniciar():
    lbl_resultados.config(text='')
    lbl_primeros.config(text='')
    lbl_ultimos.config(text='')
tk.Button(text='Reiniciar',command=reiniciar,foreground='red',font=('Arial',12,'bold')).pack(pady=15)
def mostrar_grafico():
    fig,ax = plt.subplots()
    ax.bar(df['Nombre'],df['Ganancias'],color='red')
    ax.set(title='Ventas Anuales',xlabel='Nombres',ylabel='Ganancias')
    plt.show()
tk.Button(ventana,text='MOSTRAR GRÁFICO',command=mostrar_grafico,foreground='purple',font=('Arial',12,'bold')).pack(pady=15)


ventana.mainloop()