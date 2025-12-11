# Q-Learning completo para navegación en laberinto
#Importar librerías
import numpy as np
import matplotlib.pyplot as plt
import random

def crear_laberinto(tamaño,porcentaje_paredes=20,inicio=(0,0),meta=None):
  laberinto = np.zeros((tamaño,tamaño))
  num_paredes= int((tamaño*tamaño)*porcentaje_paredes/100)
  #Ubicar paredes
  for pared in range(num_paredes):
    x,y = random.randint(0,tamaño-1),random.randint(0,tamaño-1)
    #Cuidar que inicio y meta no sean paredes
    if (x,y) != inicio and (meta is None or (x,y) != meta):
      laberinto[x,y] = 1
  #Ubicar la meta
  if meta:
    laberinto[meta] = 9 #Representa la meta con 9
  else:
    #Ubicar la meta aleatoriamente si no está especificado
    while True:
      x,y = random.randint(0,tamaño-1),random.randint(0,tamaño-1)
      if laberinto[x,y] ==  0 and (x,y) != inicio:
        laberinto[x,y] = 9
        break
  return laberinto #Devolvemos el laberinto

def ver_laberinto(laberinto):
  plt.figure(figsize=(5,5))
  plt.imshow(laberinto,cmap='gray',interpolation='nearest')
  plt.colorbar()

#Ejemplo de crear y mostrar laberinto
laberinto = crear_laberinto(10,20,inicio=(0,0),meta=(9,9))
ver_laberinto(laberinto) #Visualizamos el laberinto

#Parámetros para el algoritmo
dimensiones= (10,10)
acciones = [(0,-1),(0,1),(-1,0),(1,0)]
num_estados = 100
num_acciones = len(acciones) #4
Q = np.zeros((num_estados,num_acciones))


#Parámetros importantes
alpha = 0.1 #Tasa de aprendizaje
gamma = 0.9 #Factor de descuento
epsilon = 0.1 #Equilibrio entre exploración y explotación
episodios = 500

#función para elegir acciones equilibrando entre explotación y exploración
def elegir_accion(Q,estado,tamanio_estado):
  if random.uniform(0,1) < epsilon:
    return random.randint(0,3) #4 posibles movimientos
  else:
    return np.argmax(Q[estado]) #El indice máximo de Q

#Función para simular la acción en el laberinto
def realizar_accion(estado,accion,laberinto,tamanio):
  fila,columna = divmod(estado,tamanio) #Division entera
  if accion==0 and fila>0: 
    fila-=1
  elif accion==1 and fila<tamanio-1:
    fila+=1
  elif accion==2 and columna>0:
    columna-=1
  elif accion==3 and columna<tamanio-1:
    columna+=1

  siguiente_estado = fila*tamanio+columna
  if laberinto[fila,columna] ==1:
    recompensa=-100 #Penalización por golpear muro
    siguiente_estado = estado
    terminado = False
  elif laberinto[fila,columna] ==9:
    recompensa=100 #Recompensa por alcanzar el objetivo
    terminado = True
  else:
    recompensa=-1
    terminado = False
  return siguiente_estado,recompensa,terminado

  


#Función principal para ejecutar el algoritmo Q-Learning
def ejecutar_modelo(laberinto,tamanio,inicio,meta): 
  for episodio in range(episodios):
    estado = inicio
    terminado = False
    while not terminado:
      accion = elegir_accion(Q,estado,tamanio)
      siguiente_estado,recompensa,terminado = realizar_accion(estado,accion,laberinto,tamanio)
      #Actualizar valor Q
      Q[estado,accion] += alpha*(recompensa+gamma*np.max(Q[siguiente_estado]) -Q[estado,accion])#Con esto actualizamos el valor de Q
      estado = siguiente_estado #Actualizamos el estado
  return Q



#Función par convertir coordenadas a índice lineal
def coordenadas_a_indice(posicion,tamanio): #Recibe de argumento las coordenadas y laberinto
  return posicion[0]*tamanio+posicion[1] #Devuelve el índice lineal 

#Iniciar el laberinto y configurar el algoritmo Q-Learning
tamanio = 10
posicion_inicio = (0,0)
posicion_meta = (9,9)
laberinto = crear_laberinto(tamanio,20,inicio=posicion_inicio,meta=posicion_meta)
inicio = coordenadas_a_indice(posicion_inicio,tamanio)
meta = coordenadas_a_indice(posicion_meta,tamanio)
valores_q = ejecutar_modelo(laberinto,tamanio,inicio,meta)

#Función para mostrar el aprendizaje del agente
def mostrar_camino(laberinto,Q,inicio,meta,tamanio): #Toma como argumento laberinto,Q,inicio,meta,tamanio
  fila,columna = divmod(inicio,tamanio)
  ruta = [(fila,columna)]
  estado = inicio
  while estado!=meta: #Mientras no haya terminado
    accion = np.argmax(Q[estado])
    estado,_,_ = realizar_accion(estado,accion,laberinto,tamanio)
    fila,columna = divmod(estado,tamanio)
    ruta.append((fila,columna))
  #Mostrar el camino aprendido sobre el laberinto
  plt.figure(figsize=(5,5))
  plt.imshow(laberinto,cmap='gray',interpolation='nearest')
  filas,columnas = zip(*ruta)
  plt.plot(columnas,filas,marker='x',color='c')
  plt.colorbar() #Muestra cuál es el mejor camino encontrado

#Visualizar el resultado
mostrar_camino(laberinto,valores_q,inicio,meta,tamanio) #Mostramos el laberinto resuelto