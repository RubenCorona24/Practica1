import plotly.graph_objects as go
#Podemos modificar trazados(traces), layouts, marcadores, títulos, etcétera
#Creamos una figura con dos trazados y layout básico
fig = go.Figure()

fig.add_trace(go.Scatter(x=[1,3,6,9,12],
                         y=[16,19,26,34],
                         mode='lines',
                         name='linea')) #Le ponemos "linea" de nombre al trazado

fig.add_trace(go.Bar(x=[2,4,6,8,10],
                         y=[13,16,19,21],
                         name='barras')) #Le ponemos "barras" de nombre al trazado

#Agregamos layout (titulo,etiquetas ejes x-y)
fig.update_layout(title='Gráficos de Barras y Dispersión',
                  xaxis_title='Eje X',
                  yaxis_title='Eje Y')
#1.- Color y ancho de línea de las barras
fig.update_traces(selector=dict(name='linea'),
                  line=dict(color='purple',width=4))

fig.update_traces(selector=dict(name='barras'),
                  marker=dict(color='orange')) #Cambiamos el color de las barras
#3.- Ancho de espacio entre barras
fig.update_layout(bargap=0.4)

#1.- Modificar el título princial: agregando subtítulo, font, size, color, y centrando el texto con "fig.update_layout"
fig.update_layout(title=dict(
    text='Gráfico Lineal y de Barras<br><sup>Subtítulo del Gráfico</sup>',
    font=dict(size=24,color='red',family='Times New Roman'),
    x=0.5,
    xanchor='center' #Centramos el texto
))

#2.- Personalizamos el título de los ejes
fig.update_layout(xaxis_title=dict(font=dict(size=18,color='yellow',family='Arial')),
                                   yaxis_title=dict(font=dict(size=18,color='purple',family='Arial')))

#Modificamos el formato de los ejes
fig.update_layout(xaxis=dict(
    showgrid=True,
    gridcolor='lightgray',
    zeroline=True,
    zerolinecolor='red',
    showline=True,
    linecolor='black',
    linewidth=2
),
                  yaxis=dict(
    showgrid=True,
    gridcolor='lightgray',
    zeroline=True,
    zerolinecolor='red',
    showline=True,
    linecolor='black',
    linewidth=2
))

#--------------------Modificamos parámetros de la leyenda--------------------
fig.update_layout(
  legend=dict(orientation='h',
      x=0.3,
      y=0.9,
      bgcolor='white',
      bordercolor='black', #color de los bordes
      borderwidth=2, #ancho de los bordes
      font=dict(size=16,family='Arial') #fuente
  )
)
#-------------Insertar anotación en el gráfico------------------
#Insertar anotación con fig.add_anotation()
fig.add_annotation(
    x=3,y=19,
    text='Punto clave', #anotación
    showarrow=True, #mostrar flecha
    arrowhead=5, #tamaño de la flecha
    ax=20,ay=-30 #desplazamiento de ejes
)

#-------------------------Modificar una anotación con fig.add_annotation()
fig.add_annotation(
    x=3,y=19,
    text='Punto clave', #anotación
    showarrow=True, #mostrar flecha
    arrowhead=2, #tamaño de la flecha
    ax=-50,ay=-50,
    align='center',
    arrowcolor='blue',
    arrowsize=1,
    arrowwidth=2,
    bordercolor='black',
    borderwidth=2,
    borderpad=4,
    bgcolor='green',
    opacity=0.5) #Opacidad

#-------------------------Mostramos la figura resultante-------------------------
fig.show()