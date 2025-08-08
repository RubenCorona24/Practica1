import tkinter as tk
def presentar(name,country,empleado):
    return f"Hola, mi nombre es {name}, soy de {country}, y soy empleado en {empleado} "

def acceder(código):
    while True:
        try:
            code = int(input("Código de acceso: "))
            if code == código:
                print("Está bien. tu código es correcto")
                break
            else:
                print("Tu código es incorrecto")
        except:
            print("Debes de ingresar números")

def abrir_ventana():
    comenzar =  True
    while comenzar:
        respuesta = input("¿Quieres entrar en una ventana de tkinter?(si/no): ")
        if respuesta == 'si':
            print("Ya mismo de direccionamos a la ventana de tkinter")
            ventana = tk.Tk()
            ventana.title("SIMULACIÓN DE ERRORES")
            titulo = tk.Label(ventana,text='SIMULADOR DE ERRORES',foreground='green',font=('Arial',16,'bold'))
            titulo.pack()
            tk.Label(ventana,text='USUARIO',foreground='black',font=('Arial',12,'bold')).pack()
            entrada =tk.Entry()
            entrada.pack()
            label_asegurado = tk.Label(ventana)
            def comprobar_simulacion():
                r = entrada.get()
                if r == 'Rubén Santiago':
                    label_asegurado.config(text='Bienvenido a tu navegador Rubén',foreground='green',font=('Arial',11,'bold'))
                    label_asegurado.pack()
                else:
                    label_asegurado.config(text='Usuario incorrecto',foreground='red',font=('Arial',11,'bold'))
                    label_asegurado.pack()
            tk.Label(text='CONTRASEÑA DEL USUARIO',foreground='black',font=('Arial',12,'bold')).pack()
            entrada_contraseña = tk.Entry()
            entrada_contraseña.pack()
            label_contra = tk.Label(ventana)
            label_contra.pack()
            def comprobar_contraseña():
                contraseña = entrada_contraseña.get()
                if contraseña == '333':
                    label_contra.config(text='CONTRASEÑA CORRECTA',foreground='green',font=('Arial',12,'bold'))
                else:
                    label_contra.config(text='CONTRASEÑA INCORRECTA',foreground='red',font=('Arial',12,'bold'))

            boton_simulacion = tk.Button(ventana,text='COMPROBAR USUARIO',command=comprobar_simulacion,foreground='blue')
            boton_simulacion.pack()
            tk.Button(ventana,text='COMPROBAR CONTRASEÑA',command=comprobar_contraseña,foreground='blue').pack()
            def asegurar_contraseñas():
                if entrada.get() == 'Rubén Santiago' and entrada_contraseña.get() == '333':
                    boton_redireccionar.config(state='normal')
                else:
                    pass
            tk.Button(ventana,command=asegurar_contraseñas,text='ASEGURAR',foreground='purple',font=('Arial',12,'bold')).pack()


            def redireccionar():
                    top_level = tk.Toplevel()
                    top_level.title('Entrada top level')
                    tk.Label(top_level,text='FELICIDADES, INTRODJISTE LAS CONTRASEÑAS CORRECTAS',font=('Arial',12,'bold'),foreground='brown').pack()
                    def cerrar():
                        top_level.destroy()
                        ventana.destroy()
                    tk.Button(top_level,text='CERRAR',command=cerrar,foreground='red',font=('Arial',12,'bold'),pady=10).pack()
                    top_level.mainloop()
            boton_redireccionar = tk.Button(ventana,text='REDIRECCIONAR',command=redireccionar,foreground='purple',font=('Arial',12,'bold'),state='disabled')
            boton_redireccionar.pack()


            ventana.mainloop()
        elif respuesta == 'no':
            print("Muchas gracias por su atención")
            comenzar = False
        else:
            print("No has dado una respuesta clara")
abrir_ventana()

            