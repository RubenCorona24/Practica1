#Vamos a hacer limpieza y sustitición de datos faltantes en arrays de numpy
import numpy as np
array = np.array([10,20,np.nan,30,40,50]) #Array con un valor faltante (no válido)
#Conocer si hay un valor faltante en mi array
faltantes = np.isnan(array)
#Para conocer el promedio del array ignorando el nan, utilizamos np.nanmean()
promedio = np.nanmean(array)
#Reemplazar los valores nan con un 0 en el array
array_con_0 = np.where(np.isnan(array),0,array)
#Ahora lo reemplazamos pero con el promedio en vez de 0
array_con_promedio = np.where(np.isnan(array),promedio,array)
#Array filtrado que oculta los valores no válidos
array_filtrado = array[np.isfinite(array)]

print(f"Array original:\n{array}\n")
print(f"\nArray booleano de faltantes:\n{faltantes}\n")
print(f"\nPromedio del array sin el nan:\n{promedio}\n")
print(f"\nArray con valor 0 sustituido en los no válidos:\n{array_con_0}\n")
print(f"\nArray con el promedio sustitudo en los no válidos:\n{array_con_promedio}\n")
print(f"\nArray filtrado sin los no válidos:\n{array_filtrado}\n")