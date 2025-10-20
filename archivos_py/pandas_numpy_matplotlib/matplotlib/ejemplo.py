import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 1 fila, 2 columnas de gráficos
fig, ax = plt.subplots(1, 2)

# Primer gráfico (izquierda)
ax1 = ax[0]
ax1.plot(x,y1,color='blue')
ax1.set_title("Seno")
ax1.grid(True)

# Segundo gráfico (derecha)
ax2 = ax[1]
ax2.plot(x,y2,color='red')
ax2.set_title("Coseno")
ax2.grid(True)

# Título general de la figura
fig.suptitle("Funciones Trigonométricas", fontsize=14)

plt.show()