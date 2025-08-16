import numpy as np #Impportamos la librería numpy con el alias np
#Ejercicios de arrays con numpy
#Creamos arrays de (3,3), con números aleatorios de 0 1 10
A = np.random.randint(1,10,(3,3))
B = np.random.randint(1,10,(3,3))
print(f"Array A: \n{A}")
print('-' * 30)
print(f"Array B: \n{B}")
print('-' * 30)
C = A == B #Array que muestra valores (True/False) donde los arrays de cada posición son iguales
print(f"Comparación de los arrays en valores booleanos:\n{C}")
print('-' * 30)
print(f"Valores únicos de B: {np.unique(B)}") #Extraemos los valores únicos de el array B
print('-' * 30)
D = A.reshape((1,9)) #Modificamos la forma del array A sin cambiar valores
print(F"Array A modificado: {D}")
print('-' * 30)
print(f"Elementos de A mayores a 5:\n{A[A>5]}") #Filtramos los elementos de A que son mayores a 5
E = np.sort(B) #Ordenamos los elementos de cada fila de B
print('-' * 30)
print(f"Array B ordenada por filas:\n{E}")
F = D.T #Transpuesto el array D, de donde habiamos cambiado la forma del array A
print('-' * 30)
print(f"Array D transpuesto: {F}")
print('-' * 30)
G = np.array([2,3,4,5,7,8]) #Creamos un array de primera dimensión
print(f"Array de primera dimensión: {G}")
print('-' * 30)
H = np.array([[1,2,3,4],[5,6,7,8]]) #Creamos un array de segunda dimensión
print(F"Array de segunda dimensión: {H}")






