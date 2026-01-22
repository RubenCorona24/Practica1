
#Plotly: sirve para crear gráficos y visualizaciones de datos altamente interactivos 
#(zoom, mover, hacer clic, etc.) para explorar y presentar información de forma atractiva

#1.- Importamos libreria de plotly.graph_objects con alias "go"
import plotly.graph_objects as go


#2.- Creamos la figura (contenedor principal de plotly) dentro se encuentran todos los elementos del gráfico
fig = go.Figure()

#3.- Trazados: Representaciones de los datos en el gráfico - agregar gráfica (lineas,barras,etc)
trazado = go.Scatter(x=[1,2,3,4,5],y=[10,11,12,13,14],
                     mode = 'lines+markers', name='Dispersión') #al especificar markers, decimos que sea un gráfico de dispersión

#Agregamos el trazado a la figura con "fig.add_trace()"
fig.add_trace(trazado)

#Insertamos layout: lo que define la apariencia del gráfico
fig.update_layout(title='Gráfico de Dispersión Plotly',
                  xaxis_title='Eje x',
                  yaxis_title='Eje y')


try:

    fig.show() #Mostramos la figura
except Exception as e:
    print(f"Error, {e}")

