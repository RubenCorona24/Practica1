#VAMOS A TRABJAR CON FUNCIONES LAMBDA
#Es una función anónima (sin nombre) escrita en una sola línea
import tkinter as tk
#Primero los argumentos: la expresion
#lambda argumentos:expresion
numeros = [1,2,3,4,5,6,7,8]
#suma = lambda x,y: x + y
#print(suma(4,6))  #Función de suma lambda

#doble = lambda n: n*2
#print(doble(6)) #Función de doble lambda
#def es_par(num):
 #   if num%2 == 0:
 #       return True
#usando filter con una función común
#numeros_pares = filter(es_par,numeros)

#creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda numero:numero%2==0,numeros)
print(list(numeros_pares))

#OTRO EJEMPLOS

  #ordenar una lista de tuplas por el segundo valor
personas = [("Ana", 22), ("Luis", 30), ("Carla", 25)]
ordenado = sorted(personas, key=lambda x: x[1])
print(ordenado)
#Ejemplo con tkinter
ventana = tk.Tk()
boton= tk.Button(ventana,text='SALUDAR',command=lambda:print("!Hola!"))
boton.pack()


ventana.mainloop()