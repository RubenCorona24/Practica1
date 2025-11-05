import seaborn as sns
import matplotlib.pyplot as plt

#Cargamos el dataset de diamantes
diamonds = sns.load_dataset("diamonds")
#Función para explorar las características del dataset
def info_data():
    print(diamonds.head(5)) #Primerops 5 datos
    print(diamonds.tail(5)) #últimos 5 datos
    print(diamonds.describe)
    print(diamonds.isnull().sum()) #Valores nulos
    print(diamonds.info) #Cero nulos

def graficos():
    g = sns.relplot(diamonds,x='depth',y='price',hue='color')
    g.set_axis_labels("Profundidad",'Precio')
    g.set_titles("Relación profundidad con Precio")
    plt.suptitle("Comparación Profundidad/Precio de Diamantes")
    plt.show()

 #Llamamos a la función

def graph_dist():
    g = sns.displot(diamonds,x='carat',kde=True,kind='hist',fill=True)
    g.set_xlabels("Características del Diamante")
    plt.suptitle("Características y disponibilidad")
    plt.show()


def graph_cat():
    g = sns.catplot(diamonds,x='cut',y='price',kind='bar',hue='color')
    g.set_axis_labels("Tipo de corte",'Precio Diamante') #Agregamos título a los ejes
    g.add_legend()
    plt.suptitle("Comparación categórica Precio/Cortes") #Agregamos el título
    plt.show()
graph_cat()
plt.sca