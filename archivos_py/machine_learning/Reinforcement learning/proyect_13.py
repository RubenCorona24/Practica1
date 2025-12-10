# Q-Learning completo para navegación en laberinto
import numpy as np
import matplotlib.pyplot as plt
import random

# --------------------
# 0) Funciones base (tu código corregido de crear/ver laberinto)
# --------------------
def crear_laberinto(tamaño, porcentaje_paredes=20, inicio=(0,0), meta=None, seed=None):
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
    laberinto = np.zeros((tamaño, tamaño), dtype=int)
    num_paredes = int((tamaño*tamaño) * porcentaje_paredes / 100)

    for _ in range(num_paredes):
        x, y = random.randint(0, tamaño-1), random.randint(0, tamaño-1)
        if (x, y) != inicio and (meta is None or (x,y) != meta):
            laberinto[x, y] = 1

    if meta:
        laberinto[meta] = 9
    else:
        while True:
            x, y = random.randint(0, tamaño-1), random.randint(0, tamaño-1)
            if laberinto[x, y] == 0 and (x,y) != inicio:
                laberinto[x,y] = 9
                break
    return laberinto

def ver_laberinto(laberinto, camino=None):
    plt.figure(figsize=(6,6))
    cmap = plt.get_cmap('gray_r')
    plt.imshow(laberinto, cmap=cmap, interpolation='nearest')
    plt.title("Laberinto (0=camino,1=pared,9=meta)")
    # si hay camino, dibujarlo encima
    if camino:
        xs = [p[1] for p in camino]  # columnas = x en plot
        ys = [p[0] for p in camino]  # filas = y en plot
        plt.plot(xs, ys, marker='o', linewidth=2, markersize=6, color='red')
        plt.scatter(xs[0], ys[0], s=100, marker='s', label='Start', c='green')
        plt.scatter(xs[-1], ys[-1], s=100, marker='*', label='Goal', c='yellow')
        plt.legend()
    plt.gca().invert_yaxis()
    plt.show()

# --------------------
# 1) Parámetros para Q-Learning
# --------------------
alpha = 0.1       # tasa de aprendizaje
gamma = 0.95      # descuento
epsilon = 0.2     # exploración inicial
episodios = 2000  # episodios
acciones = [(-1,0),(1,0),(0,-1),(0,1)]  # arriba, abajo, izquierda, derecha

# --------------------
# 5) Función para convertir coordenadas a índice lineal y viceversa
# --------------------
def coord_a_indice(coord, tamaño):
    x, y = coord
    return x * tamaño + y

def indice_a_coord(idx, tamaño):
    x = idx // tamaño
    y = idx % tamaño
    return (x, y)

# --------------------
# 2) Función ε-greedy para elegir acción
# --------------------
def elegir_accion(idx_estado, Q, epsilon):
    if random.random() < epsilon:
        return random.randint(0, len(acciones)-1)
    else:
        return int(np.argmax(Q[idx_estado]))  # asegurar int

# --------------------
# 3) Función para simular la acción en el laberinto
# --------------------
def simular_accion(laberinto, pos, accion_idx):
    tamaño = laberinto.shape[0]
    dx, dy = acciones[accion_idx]
    nx, ny = pos[0] + dx, pos[1] + dy

    # fuera de límites -> penalizar y quedarse
    if nx < 0 or nx >= tamaño or ny < 0 or ny >= tamaño:
        return pos, -5, False

    valor = laberinto[nx, ny]

    # pared
    if valor == 1:
        return pos, -50, False

    # meta (9)
    if valor == 9:
        return (nx, ny), 100, True

    # movimiento normal
    return (nx, ny), -1, False

# --------------------
# 4) Función principal: ejecutar_modelo (entrenamiento Q-Learning)
# --------------------
def ejecutar_modelo(laberinto, Q, episodios, alpha, gamma, epsilon,
                    inicio=(0,0), decay_eps=True, min_epsilon=0.01, verbose=False):
    tamaño = laberinto.shape[0]
    for ep in range(episodios):
        pos = inicio
        idx = coord_a_indice(pos, tamaño)
        terminado = False

        # opcional: decrementar epsilon
        if decay_eps:
            eps = max(min_epsilon, epsilon * (1 - ep/episodios))
        else:
            eps = epsilon

        pasos = 0
        while not terminado and pasos < tamaño*tamaño*10:  # límite de pasos por episodio
            accion_idx = elegir_accion(idx, Q, eps)
            nueva_pos, recompensa, terminado = simular_accion(laberinto, pos, accion_idx)
            idx_nuevo = coord_a_indice(nueva_pos, tamaño)

            # actualización Q-Learning (correcta: multiplicar por alpha)
            Q[idx, accion_idx] += alpha * (recompensa + gamma * np.max(Q[idx_nuevo]) - Q[idx, accion_idx])

            pos = nueva_pos
            idx = idx_nuevo
            pasos += 1

        if verbose and (ep % (episodios//5) == 0):
            print(f"Episodio {ep}/{episodios}, epsilon={eps:.3f}, pasos={pasos}")

    if verbose:
        print("Entrenamiento finalizado.")
    return Q

# --------------------
# 7) Función para mostrar el aprendizaje del agente (reconstruir camino)
# --------------------
def reconstruir_camino(Q, laberinto, inicio=(0,0), max_steps=1000):
    tamaño = laberinto.shape[0]
    pos = inicio
    camino = [pos]
    terminado = False
    pasos = 0

    while (not terminado) and pasos < max_steps:
        idx = coord_a_indice(pos, tamaño)
        accion_idx = int(np.argmax(Q[idx]))
        nueva_pos, _, terminado = simular_accion(laberinto, pos, accion_idx)
        # si no se mueve (por pared o fuera) salir para evitar bucle infinito
        if nueva_pos == pos:
            break
        camino.append(nueva_pos)
        pos = nueva_pos
        pasos += 1

    return camino, terminado

# --------------------
# 6) Iniciar laberinto y configurar Q
# --------------------
tamaño = 10
laberinto = crear_laberinto(tamaño, porcentaje_paredes=20, inicio=(0,0), meta=(9,9), seed=42)
ver_laberinto(laberinto)

num_estados = tamaño * tamaño
num_acciones = len(acciones)
Q = np.zeros((num_estados, num_acciones))

# --------------------
# Ejecutar entrenamiento
# --------------------
Q = ejecutar_modelo(laberinto, Q, episodios=episodios, alpha=alpha, gamma=gamma, epsilon=epsilon, inicio=(0,0), decay_eps=True, verbose=True)

# --------------------
# 8) Visualizar resultado: reconstruir y mostrar camino
# --------------------
camino, alcanzada = reconstruir_camino(Q, laberinto, inicio=(0,0))
print("Meta alcanzada en la reconstrucción?" , alcanzada)
print("Longitud del camino reconstruido:", len(camino))
ver_laberinto(laberinto, camino=camino)