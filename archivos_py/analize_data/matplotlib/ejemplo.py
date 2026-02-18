import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#---------EJEMPLO CON NUMPY & MATPLOTLIB----------
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

#-----------EJEMPLO CON PANDAS Y MATPLOTLIB------------
#AHORA CREAMOS UN DATAFRAME
df = pd.DataFrame({
    'Modelo': ['Carro Nissan','Volkswagen',  'Toyota ','Chevrolet aveo HB'],
    'Vendidas': [255116,138181,121968,34465],
    'Precio': [266900,318854,316400,287400]
})

#Agregar un ingreso total
df['Ingreso Total'] = df['Vendidas'] * df['Precio']
print(df)
def info_data(df):
    #Encontrar cuantos autos en total vendidos
    total = sum(df['Vendidas'])
    #Encontrar cuál es el precio más alto y su modelo
    precio_max = max(df["Precio"])
    modelo_caro = df.loc[df['Precio'].idxmax(),'Modelo']
    print(f"El total de autos vendidos es de: {total}\nEl precio más alto de los carros es de ${precio_max}mxm del modelo {modelo_caro}")

def graficar_datos():
    fig, axs = plt.subplots(1,3,figsize=(14,5))
    ax1 = axs[0]
    ax1.bar(df['Modelo'],df['Ingreso Total'])
    ax1.set_title("Gráfico de barras Modelo/Ingresos totales")
    ax1.set_xlabel("Modelos")
    ax1.set_ylabel("Ingresos totales")
    ax1.grid(True,linestyle='--',alpha=0.6)
    #Segundo gráfico de lineas (precio unitario por producto)
    ax2 = axs[1]
    ax2.plot(df['Modelo'],df['Precio'],label="Precio Unitario")
    ax2.set_title("Gráfico de línea Modelo/Precio")
    ax2.set_xlabel("Modelos")
    ax2.set_ylabel("Precio Unitario")
    ax2.legend()
    ax2.grid(True,linestyle='--',alpha=0.6)
    #Tercer gráfico de pastel (porcentaje de ingresos por producto)
    ax3 = axs[2]
    ax3.pie(df['Vendidas'],labels=df['Modelo'],autopct='%1.1f%%',shadow=True,explode=(0.1,0,0,0),colors=['red','yellow','orange','green'])
    ax3.set_title("Gráfico de pastel Modelo/Cantidad vendida")
    ax3.grid(True,linestyle='--',alpha=0.6)
    fig.suptitle("Análisis de Ventas de Modelos Año 2025",fontsize=16)
    plt.tight_layout()
    plt.savefig("archivos_aparte/análisis_ventas_modelos_2025.png",dpi=300)
    plt.show()
    

graficar_datos()