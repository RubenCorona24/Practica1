#Primero importamos matplotlib como plt
import matplotlib.pyplot as plt
#Mediante esta librría creamos gráficos, lineales, barras, histogramas, etc
x = (1,2,3,4,5,6,7,8,9)

y = []
for n in x:
    y.append(n**2) #Agregamos el valor de x al cuadrado a y

plt.plot(x,y)
plt.title("Explicación de Matplotlib")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()