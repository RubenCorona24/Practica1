#Algoritmo de aprendizaje por reforzamiento: q learning
#importamos librerias necesarias
import numpy as np
import random

#Representación del ambiente
dimensiones = (5,5) #tabla de 5x5 (25)
estado_inicial = (0,0) #Estado inicial
estado_objetivo = (4,4) #Nuestro estado objetivo
obstaculos = [(1,1),(1,3),(2,3),(3,0)] #Coordenadas de obstáculos
acciones = [(-1,0),(1,0),(0,-1),(0,1)] #Las acciones: (-1,0) arriba, (1,0) abajo, (0,-1) Izquierda, (0,1) Derecha

#Calcular posiciones posibles de la tabla (25)
num_estados = dimensiones[0] * dimensiones[1]
#Calcular las acciones que puede hacer el agente (4)
num_acciones = len(acciones)

#Función para convertir de estado a índice
def estado_a_indice(estado):
    return estado[0] * dimensiones[1] + estado[1] #Convierte las coordenadas, en un índice de 0 a 24

#Creamos la tabla q
Q = np.zeros((num_estados,num_acciones)) #Tiene una dimension de 25x4

#Parámetros clave del algoritmo (alpha,gamma,epsilon,episodios)
alpha = 0.1 #Tasa de aprendizaje
gamma = 0.99 #Factor de descuento (importancia de recompensas futuras)
epsilon = 0.2 #Realizar una acción aleatoria (exploración)
episodios = 100 #Numero total de veces de proceso de entrenamiento(empieza con estado inicial, termina en el estado objetivo)

#Función de elegir accion
def elegir_accion(estado):
    if random.uniform(0,1) >epsilon:
        return random.choice(acciones) #Elige aleatoriamente una acción de "acciones"
    else:
        return np.argmax(Q[estado_a_indice(estado)])

#Función de aplicar acción
def aplicar_accion(estado,accion_idx):
    accion = acciones[accion_idx]
    nuevo_estado = tuple(np.add(estado,accion) % dimensiones)
    if nuevo_estado in obstaculos or nuevo_estado == estado:
        return estado,-100,False #Devuelve estado, recompensa de -100 y False(no termina juego)
    if nuevo_estado == estado_objetivo:
        return nuevo_estado,100,True #Devuelve nuevo estado, recompensa +100 y True(termina juego)
    return nuevo_estado,-1,False #Devuelve nuevo estado, recompensa de -1 y False(no termina juego)

#Iteramos con ciclo for
for episodio in range(episodios): #Se repite 100 veces
    estado = estado_inicial
    terminado = False
    while not terminado: #Mientras todavía no se acabe el juego
        idx_estado = estado_a_indice(estado)
        accion_idx = elegir_accion(estado)
        if isinstance(accion_idx,tuple):
            accion_idx = acciones.index(accion_idx)
        nuevo_estado, recompensa,terminado = aplicar_accion(estado,accion_idx)
        idx_nuevo_estado = estado_a_indice(nuevo_estado) #Nuevo indice de estado
        #Actualizamos el valor de Q
        Q[idx_estado,accion_idx] = Q[idx_estado,accion_idx] + alpha * (recompensa+gamma*np.max(Q[idx_nuevo_estado]) - Q[idx_estado,accion_idx])
        estado = nuevo_estado
politica = np.zeros(dimensiones,dtype=int)
for i in range(dimensiones[0]):
    for j in range(dimensiones[1]):
        estado = (i,j)
        idx_estado = estado_a_indice(estado)
        mejor_accion = np.argmax(Q[idx_estado])
        politica[i,j] = mejor_accion
print(f"Política aprendida: (0:arriba,1:abajo,2:izquierda,3:derecha)")
print(politica) #Imprime mapa 5x5 con la mejor acción por cada estado