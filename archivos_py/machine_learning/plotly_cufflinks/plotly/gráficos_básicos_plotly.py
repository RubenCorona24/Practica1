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

