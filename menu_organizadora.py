import tkinter as tk


def inicio():
    print("Bienvenido al organizador de contenedores de basura")
    depositos = []
    while True:
        eleccion = input("¿De qué tipo es la basura? -1-ORGÁNICA-  -2-NO ORGÁNICA- -3:SALIR- -4:VER BASURA- -5:ABRIR VENTANA- : ")
        if eleccion == '1':
            print("Tu basura es orgánica")
            basura = input("Deposita tu basura: ")
            depositos.append(basura)
        elif eleccion == '2':
            print("Tu basura es inorgánica")
            basura = input("Deposita tu basura, objeto: ")
            depositos.append(basura)
        elif eleccion == '3':
            print("GRacias por tu elecciión, hasta luego!!")
            break
        elif eleccion =='4':
                if len(depositos) == 0:
                     print("Aún no hay depósitos")
                else:
                     
                    print("Vale, verás los depósitos que por ahora has dejado")
                    print(f"DEPÓSITOS: {depositos}")
        elif eleccion == '5':
             print("Abriendo ventana")
             ventana = tk.Tk()
             ventana.title("Mi Ventana")
             ventana.geometry("600x900")
             label = tk.Label(ventana,text='SOY LABEL, ESCOGISTE OPCIÓN 5',fg='red')
             label.pack()
             def cambiar_texto():
                  label.config(text="DISTE CLIC EN EL BOTÓN!",font=("Arial",14,'bold'),fg='green')
             boton = tk.Button(text='Cambiar color del label',command=cambiar_texto)
             boton.pack() 
             listbox = tk.Listbox(ventana,width=30,height=10)
             listbox.insert(0,'Primer elemento')
             listbox.insert(1,'Segundo elemento')
             listbox.insert(2,'Tercerr elemento')
             listbox.pack()
             def cerrar():
                  ventana.destroy()
             boton_cerrar = tk.Button(ventana,text='CERRAR',command=cerrar) 
             boton_cerrar.pack()          
        else:
            print("Opción inválida (1/2/3/4/5)")

inicio()
