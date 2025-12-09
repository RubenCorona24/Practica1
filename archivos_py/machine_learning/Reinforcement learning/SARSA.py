#SARASA (Estado-Accion-Recompensa-Accion-Estado)
import numpy as np
import random

#Inicialización
dimensiones = (4,4)
estado_inicial = (0,0)
estado_objetivo = (3,3)
acciones = [(0,-1),(0,1),(-1,0),(1,0)]
acciones_simbolos = ['↑','↓','←','→']
num_estados = dimensiones[0] * dimensiones[1]
num_acciones = len(acciones)
Q = np.zeros((num_estados,num_acciones))

#Variables importantes
alpha = 0.1 #tasa de aprendizaje
gamma = 0.99 #Importancia de recompensas futuras
epsilon = 0.2 #Regula equilibrio entre exploración y explotación
episodios = 1000
def estado_a_indice(estado): #Argumento el estado
    return estado[0] * dimensiones[1] + estado[1]

#Crear funciones
def elegir_accion(estado):
    if random.uniform(0,1) < epsilon:
        return random.randint(0,num_acciones-1)
    else:
        return np.argmax(Q[estado_a_indice(estado)]) #Toma la decisión que sabe que es mejor

def aplicar_accion(estado,accion_idx):
    accion = acciones[accion_idx]
    nuevo_estado = tuple(np.add(estado,accion) % np.array(dimensiones))
    if nuevo_estado==estado_objetivo:
        recompensa = 1
    else:
        recompensa=-1
    return nuevo_estado,recompensa,nuevo_estado==estado_objetivo #Me puede devvolver True o False
#Convierte el resultado en una tupla

#Entrenamos al modelo 1000 veces
for episodio in range(episodios):
    estado = estado_inicial
    accion_idx = elegir_accion(estado)
    terminado = False
    while not terminado:
        nuevo_estado,recompensa,terminado = aplicar_accion(estado,accion_idx)
        nueva_accion_idx = elegir_accion(nuevo_estado)
        indice = estado_a_indice(estado)
        #Actualizamos valor SARSA
        Q[indice,accion_idx] += alpha * (recompensa+gamma*Q[estado_a_indice(nuevo_estado),nueva_accion_idx] - Q[indice,accion_idx])
        #Actualizamos variables
        estado,accion_idx = nuevo_estado,nueva_accion_idx

politica_simbolos = np.empty(dimensiones,dtype='<U2') #Crea un array vacío
for i in range(dimensiones[0]):
    for j in range(dimensiones[1]):
        estado = (i,j)
        mejor_accion = np.argmax(Q[estado_a_indice(estado)])
        politica_simbolos[i,j] = acciones_simbolos[mejor_accion]
print(f"-------Política aprendida de mejor acción por estado--------")
print(politica_simbolos)