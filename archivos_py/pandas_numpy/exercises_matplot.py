import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10,10,100) #Genera 100 puntos igualmente espaciados entre -10 y 100
y = np.sin(x) #Calcula el seno de cada valor de x
fig,ax = plt.subplots()
ax.scatter(x,y) #Ahora usamos el gráfico de scatter
plt.show()



#Ahora con varios gráficos
x2 = list(range(101))
y2 = []
for n in x2:
    y2.append(n+1)

x3 = [1,10,20,30,40]
y3 = [1,2,3,4,50]

x4 = [30,60,90,120]
y4 = [100,200,300,400]

fig,((ax1,ax2),(ax3,ax4))= plt.subplots(2,2,figsize=(10,5))
ax1.plot(x,y)
ax2.plot(x2,y2)
ax3.plot(x3,y3)
ax4.plot(x4,y4)  #Creamos los 4 gráficos

plt.show()
