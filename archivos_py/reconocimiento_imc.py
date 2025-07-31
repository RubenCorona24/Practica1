from tkinter import Label, Entry


#programa de reconocimiento de personajes
personajes = []
import tkinter as tk


def reconocer(persona):
    if persona == 'Rubén Santiago':
        try:
            code = int(input("Rubén Santiago, dime tu código: "))
            if code == 332:
                print("Felicidades, has desbloqueado el código")
                ventana = tk.Tk()
                ventana.title('Premio otorgado')
                label = Label(ventana,text='HAS CONSEGUIDO EL PREMIO',font=('Arial',20,'bold'),foreground='green')
                def conseguir_premio():
                    label.pack(side='top')

                boton = tk.Button(ventana,text='CONSEGUIR PREMIO',command=conseguir_premio)
                boton.pack()
                ventana.mainloop()
            else:
                print("Rubén Santiago, tu código es incorrecto")
        except:
            print("Debe ser un código de 3 dígitos")
    else:
        print("***Usuario Incorrecto, volver a intentar***")
def medir_imc():

    ventana = tk.Tk()
    ventana.title('CALCULADORA DE IMC')
    Label(ventana, text="Altura en metros:").pack()
    entrada_altura = Entry(ventana)
    entrada_altura.pack()
    Label(ventana, text="Peso en kg:").pack()
    entrada_peso = Entry(ventana)
    entrada_peso.pack()
    label_mostrar = Label(ventana,font=('Arial',12,'bold'),foreground='green')
    label_despedida = Label(ventana)
    def mostrar():
        try:
            peso = float(entrada_peso.get())
            altura = float(entrada_altura.get())
            imc = peso / (altura ** 2)
            label_mostrar.config(text=f"Tu IMC es: {round(imc, 2)}")
            label_mostrar.pack()
            label_despedida.config(text='MUCHAS GRACIAS POR TU ELECCIÓN :)',font=('Arial',12,'bold'),foreground='black')
            label_despedida.pack()


        except ValueError:
            label_mostrar.config(text="Introduce números válidos")
            label_mostrar.pack()
    def reiniciar():
        label_mostrar.config(text='')
        label_despedida.config(text='')
        entrada_altura.delete(0,tk.END)
        entrada_peso.delete(0,tk.END)
    boton_muestra = tk.Button(ventana,text='MOSTRAR RESULTADOS',command=mostrar)
    boton_muestra.pack()
    boton_reinicio = tk.Button(ventana,text='REINICIAR',font=('Arial',12,'bold'),foreground='red',command=reiniciar)
    boton_reinicio.pack()





    ventana.mainloop()

def menu():
    while True:
        try:
            print("Bienvenido a nuestra oficina de reconocimiento")
            print("Tienes 3 opciones: 1-Salir 2-ENTRAR en modo reconocimiento 3-Medida de IMC")
            eleccion = int(input())
            if eleccion == 1:
                print("Gracias por su elección!!")
                break
            elif eleccion == 2:
                print("---Has entrado en modo de reconocimiento----")
                person = input('Dime tu nombre completo: ')
                reconocer(person)
            elif eleccion == 3:
                medir_imc()

            else:
                print("Opción inválida")
                continue
        except:
            print("Inválido, debes de seleccionar(1/2/3)")
print(menu())

