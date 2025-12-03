import pyarrow
import pandas as pd
import time
#PyArrow es una biblioteca de Python que proporciona una interfaz para el framework Apache Arrow,
#  un estándar de código abierto para el procesamiento eficiente de datos tabulares en memoria, utilizando un formato de almacenamiento columnar.
#  Actúa como un puente entre Python y otros sistemas de procesamiento de datos de alto rendimiento.

start = time.time() #Iniciamos el tiempo
df = pd.read_csv("archivos_aparte/Datos_Ventas_Tienda.csv",engine='pyarrow',dtype_backend='pyarrow')
end = time.time()
mem = df.memory_usage(deep=True).sum() / (1024**2)
print(f"Tiempo de carga con pyarrow: {end-start:.2f} segundos") #Imprimimos los segundos con dos decimales
print(f"Memoria usada: {mem:.2f} MB") #Imprimimos la memoria en MB con 2 decimales
print(df) #Imprimimos el df