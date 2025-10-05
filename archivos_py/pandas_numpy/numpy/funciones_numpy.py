#Importamos numpy
import numpy as np
def ver_propiedades_array(array):
    dimensiones = array.ndim
    forma = array.shape
    total_elementos = array.size
    print(f"El array contiene {dimensiones} dimensiones, la forma es de {forma}, y el total de elementos es de {total_elementos}")
    
#Creamos un array unidimensional
array = np.array([1,2,3,4,5,6,7,8,9])
#Cambiamos la forma del array
array_modifi = array.reshape(3,3)
#Método para voltear el array (transpose())
array_volteado = array_modifi.transpose()
#Convertir un array multidimensional en uno unidimensional con flatten (ocupa memoria, crea copia aplanada)
array_chato = array_modifi.flatten()
#Volvemos a hacer lo mismo pero con ravel (crea vista aplanada del arrat, no crea copia)
array_ravel = array_modifi.ravel()
print(f"Array original:\n{array}\n")
print(f"\nArray modificado a 3 dimensiones:\n{array_modifi}\n")
print(f"\nArray volteado:\n{array_volteado}\n")
print(f"\nArray convertido a unidimensional:\n{array_chato}\n")
print(f"\nArray convertido a unidimensional pero sin copia (ravel):\n{array_ravel}\n")