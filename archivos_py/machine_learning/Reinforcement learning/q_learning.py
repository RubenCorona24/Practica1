#Algoritmo de aprendizaje por reforzamiento: q learning
#importamos librerias necesarias
import numpy as np
import random
import pandas as pd
import time
start = time.time() #Iniciamos el tiempo
df = pd.read_csv("archivos_aparte/Datos_Ventas_Tienda.csv",engine='pyarrow',dtype_backend='pyarrow')
end = time.time()
mem = df.memory_usage(deep=True).sum() / (1024**2)
print(f"Tiempo de carga con pyarrow: {end-start:.2f} segundos") #Imprimimos los segundos con dos decimales
print(f"Memoria usada: {mem:.2f} MB") #Imprimimos la memoria en MB con 2 decimales
print(df) #Imprimimos el df