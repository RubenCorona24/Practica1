#Gráficos más importantes de plotly
import plotly.graph_objects as go

#1.- Gráfico de barras con plotly

x = [10,20,30,40,50]
y = [12,16,21,19,28]
fig = go.Figure() #Creamos figura
fig.add_trace(go.Bar(x=x,y=y,
              marker=dict(color='green',line=dict(color='black',width=1.5)))) #El marcador recibe como parámetros el color, la línea como el ancho de la barra
#Agregamos layout a la figura
fig.update_layout(title='Gráfico de Barras',xaxis_title='Eje x',
                  yaxis_title='Eje y')    

fig.show()  

#Creamos un gráfico de áreas: El mismo gráfico de líneas pero con relleno en la parte de abajo
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=x,y=y,
                          mode='lines',
                          fill='tozeroy',
                          name='Area')) #Con fill=tozeroy activamos el relleno de abajo
fig2.update_layout(title='Gráfico de áreas',
                   xaxis_title='Eje x',yaxis_title='Eje y')
fig2.show()

#Creamos un gráfico de torta (gráfico circular)
fig3 = go.Figure()
fig3.add_trace(go.Pie(labels=['A','B','C','D','E'],
                      values=[1200,1343,1900,1460])) #insertamos las etiquetas con sus respectivos valores
fig3.update_layout(title='Gráfico de pastel')
     
# Creamos un Histograma con Plotly
histograma = go.Histogram(x=[10,10,9,9,9,11,11,11,11,12,12])
fig4 = go.Figure(data=histograma)
fig4.update_layout(title='Histograma')
fig4.show()

#Realizamos un mapa de calor "heatmap"
#Creamos listas dentro de una lista dentro de la variable "z" donde almacenamos valores
z = [[1,20,30],
     [20,1,60],
     [70,30,90]]
fig5 = go.Figure(data=go.Heatmap(z=z)) #Insertamos el mapa de calor
fig5.update_layout(title='Mapa de calor')

#Creamos un gráfico de caja
fig6 = go.Figure(data=go.Box(y=[1,2,3,4,5,6,7,8,9,10]))
fig2.update_layout(title='Gráfico de Caja')

#Creamos un gráfico de dispersión con líneas "lines+markers"
fig7 = go.Figure(data=go.Scatter(x=x,y=y,mode='lines+markers'))
fig.update_layout(title='Gráfico de Líneas con marcadores')

#Creamos un gráfico de violin "violin plot"
fig8 = go.Figure()
fig8.add_trace(go.Violin(y=x,name='y0',box_visible=True,line_color='blue'))
fig8.add_trace(go.Violin(y=y,name='y1',box_visible=True,line_color='red'))
fig8.update_layout(title='Gráfico de violín')

#Creamos un gráfico de Gantt (necesitamos importar la libreria pyplot.figure_factory as ff)
import plotly.figure_factory as ff
#1.- Creamos variable df con lista de diccionarios en el cual almacenamos tareas
df = [dict(Task='Resolver problemas de código',Start='2026-01-05',Finish='2026-01-09'),
      dict(Task='Mandar pull de actualizaciones',Start='2026-01-10',Finish='2026-01-14')]
#2.- Creamos la figura con ff.create_gantt
fig9 = ff.create_gantt(df) #Pasamos de parámetro la lista con los diccionarios
fig9.update_layout(title='Diagrama de Gantt')
fig9.show()

