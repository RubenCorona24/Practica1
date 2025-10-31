import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#Jointplot: to visualize the relationship between two variables, 
# showing a central bivariate graph (such as a scatter plot) along with the marginal 
# distributions of 
# each variable on the axes.

#Cargamos el dataset de pinguinos
pinguins = sns.load_dataset("penguins")
#Visualizamos el dataset
print(pinguins)
def grafico_jointplot():
    g = sns.jointplot(data=pinguins,x='flipper_length_mm',y='bill_length_mm',hue='species')
    #hue: distribuye por categorías mediante colores (en este caso por especies)
    g.set_axis_labels("Largo de aletas (mm)","Largo del pico (mm)")
    plt.show()

def grafico_pairplot():
    sns.pairplot(pinguins,hue='species')
    plt.show()
    #Sin información para los ejes

grafico_jointplot()
grafico_pairplot()

#Ahora un ejemplo de jointplot y pairplot mediante un Dataframe
df = pd.read_csv("archivos_aparte/Top-Películas.csv")
#leemos el df
print(df)
def grafico_df_joint():
    g = sns.jointplot(data=df,x='rating',y='recaudación(M)',hue='género')
    g.set_axis_labels("Rating","Recaudación")
    plt.savefig("archivos_aparte/data_sns/graphic_movies.png")
    plt.show()


def grafico_df_pairplot():
    sns.pairplot(data=df,hue='género') #Sin datos de ejes 
    plt.savefig("archivos_aparte/data_sns/graphic_movies_pairplot.png") #Guardamos el gráfico
    plt.show()
#Vamos a crear una nueva columna para el dataframe, según sus ventas
values = []
for n in df['rating']:
    if n >8:
        data = 'buena_calificación'
    else:
        data = 'mal calificación'
    values.append(data)


df['Calificación'] = values
print(df) #Visualizamos el nuevo df con la columna
primeros_titulos = df.head(10)
#Crear un nuevo gráfico mediante la calificación
def grafico_peliculas():
    graf =sns.barplot(data=df,x=primeros_titulos['título'],y=primeros_titulos['recaudación(M)'],hue='Calificación')
    graf.set_title("Películas 2025")
    graf.set_xlabel("Título")
    graf.set_ylabel("Recaudación")
    plt.show()


def grafico_distplot():
    graf =sns.displot(data=df,x=primeros_titulos['título'],y=primeros_titulos['recaudación(M)'],hue='género',col='Calificación')
    graf.set_xticklabels(rotation=45)
    plt.show()
grafico_distplot()