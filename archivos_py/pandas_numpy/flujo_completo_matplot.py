import matplotlib.pyplot as plt

x = list(range(101)) 
y = []
for n in x:
    y.append(n**2) #Creamos nuestras coordenadas

fig,ax = plt.subplots() #Creamos la figura, y los subplots
plt.style.use()
ax.plot(x,y) #Hacemos el gráfico agregando los datos
ax.set(title='Casos de COVID 19',xlabel='Días',ylabel='Casos') #Personalizar título, etiquetas
fig.savefig("Gráfico con matplotlib.png") #Guardamos el archivo
plt.show()

