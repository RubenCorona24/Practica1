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

personas = [("Ana", 22), ("Luis", 30), ("Carla", 25)]
ordenado = sorted(personas, key=lambda x: x[1])
print(ordenado) #ordenar una lista de tuplas por el segundo valor---sorted(iterable,key=None,reverse=False)

#Ejemplo con tkinter
#ventana = tk.Tk()
#boton= tk.Button(ventana,text='SALUDAR',command=lambda:print("!Hola!"))
#boton.pack()


#ventana.mainloop()
numbers = [-3,4,6,7,5,-6]
print(list(filter(lambda num:num <=0,numbers))) #Función para Filtrar números negativos con filter()

other = [1,2,3,4]
dobles = map(lambda n:n*2,other)
print(list(dobles)) #Función para doblar cada número de una lista con map()---map(función,iterable)

names = ['Juan','Eduardo','Sabrina']
mayusculas = map(lambda name:name.upper(),names)
print(list(mayusculas)) #Función para convertir a mayusculas cada nombre de la lista con map()

palabras = ['hola', 'mundo', 'python']
longitud = map(lambda palabra:len(palabra),palabras)
print(list(longitud)) #Función para devolver longitud de cada palabra en la lista