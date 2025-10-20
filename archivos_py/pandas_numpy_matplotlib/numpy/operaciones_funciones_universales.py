import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([[10],[20],[30]])
broadcast_suma = array1+array2
broadcast_multi =array1*array2
#Funciones universales de Numpy
A =  np.array([1,2,3])
B= np.array([4,5,6])
#Con add(), sumamos cada uno de los elementos de los arrays según su posición
resultado = np.add(A,B)
#substract() - Lo mismo que add pero en resta
resultado_sub = np.subtract(A,B)
#multiply - Lo mismo pero con multiplicación
resultado_multi = np.multiply(A,B)
#.divide() - Lo mismo pero con división
resultado_divi = np.divide(A,B)
#Sacar el exponente de cada elemento del array
resultado2 = np.exp(A) #Sacamos el exponente de cada elemento del array A
#Sacar el logaritmo natural de cada número
resultado3 = np.log(A)
#Sacar la raíz de cada elemento del array
resultado4 = np.sqrt(A) #Sacamos la raiz de cada elmento del array a

print(f"Primer array:\n{array1}\nSegundo array:\n{array2}")
print(f"\nArrays sumados: {broadcast_suma}")
print(f"\narray A:\n{A}\narrayB:{B}")
print(f"\nResultado de np.add(A,B):\n{resultado}")
print(f"\nResultado de np.subtract(A,B):\n{resultado_sub}")
print(f"\nResultado de np.multiply(A,B):\n{resultado_multi}")
print(f"\nResultado de np.divi(A,B):\n{resultado_divi}")
print(f"\nResultado de np.exp(A):\n{resultado2}")
print(f"\nResultado de np.log(A):\n{resultado3}")
print(f"\nResultado de np.sqrt(A):\n{resultado4}")