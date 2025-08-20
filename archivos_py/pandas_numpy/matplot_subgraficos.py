import matplotlib.pyplot as plt
import numpy as np
# Datos
x2 = list(range(101))
y2 = [n+1 for n in x2]   # forma compacta del for

x3 = [10,20,30,40,50]
y3 = [1,2,3,4,50]

x4 = [30,60,90,120]
y4 = [100,200,300,400]

# Creamos 4 subgráficos (2 filas x 2 columnas)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 5))

# Primer gráfico (ejemplo: reusar x2,y2)
ax1.plot(x2, y2, color="blue")
ax1.set_title("Gráfico 1")

# Segundo gráfico
ax2.plot(x2, y2, color="red")
ax2.set_title("Gráfico 2")

# Tercer gráfico
ax3.plot(x3, y3, marker="o", color="green")
ax3.set_title("Gráfico 3")

# Cuarto gráfico
ax4.plot(x4, y4, linestyle="--", color="purple")
ax4.set_title("Gráfico 4")

plt.tight_layout()
plt.show()