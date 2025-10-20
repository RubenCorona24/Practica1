import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Datos experimentales
nacl_g = [0, 2.5, 7.5, 12.5]
teb_experimental = [100.0, 100.5, 101.2, 103.5]  # Asumiendo 103.5°C para 12.5g

# Cálculo de la línea de tendencia (regresión lineal)
pendiente, intercepto, r_valor, p_valor, std_err = stats.linregress(nacl_g, teb_experimental)
linea_tendencia = [intercepto + pendiente * x for x in nacl_g]

# Predicciones para 10g y 15g
prediccion_10g = intercepto + pendiente * 10
prediccion_15g = intercepto + pendiente * 15

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.scatter(nacl_g, teb_experimental, color='blue', s=100, label='Datos experimentales')
plt.plot(nacl_g, linea_tendencia, color='red', linestyle='--', label='Línea de tendencia')

# Marcar predicciones
plt.scatter([10, 15], [prediccion_10g, prediccion_15g], color='green', s=100, label='Predicciones')

# Añadir ecuación de la línea de tendencia
ecuacion = f'y = {pendiente:.3f}x + {intercepto:.3f}'
plt.text(0.5, 103.2, f'Ecuación: {ecuacion}', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

# Personalizar la gráfica
plt.title('Efecto de la concentración de NaCl en el punto de ebullición del agua', fontsize=14, pad=20)
plt.xlabel('Masa de NaCl (g) en 50 mL de agua', fontsize=12)
plt.ylabel('Temperatura de ebullición (°C)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='lower right')

# Ajustar ejes
plt.xlim(-0.5, 16)
plt.ylim(99.5, 104.5)

# Mostrar valores en los puntos
for i, (x, y) in enumerate(zip(nacl_g, teb_experimental)):
    plt.annotate(f'{y}°C', (x, y), textcoords="offset points", xytext=(0,10), ha='center')

plt.annotate(f'{prediccion_10g:.1f}°C', (10, prediccion_10g), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate(f'{prediccion_15g:.1f}°C', (15, prediccion_15g), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()

# Mostrar valores de predicción
print(f"Predicción para 10g de NaCl: {prediccion_10g:.2f}°C")
print(f"Predicción para 15g de NaCl: {prediccion_15g:.2f}°C")
