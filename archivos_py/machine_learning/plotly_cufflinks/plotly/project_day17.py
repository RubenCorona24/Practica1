#-------------DISEÑAMOS UN DASHBOARD EN BASE A DATOS DE TERREMOTO OFICIALES----------------
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import html,dcc,Input,Output

#Traemos información del dataset
df = pd.read_csv('archivos_aparte/earthquake+data.csv',index_col=False)
df['Date & Time'] = pd.to_datetime(df['Date & Time']) #Convertimos a tipo de dato de fecha
#Creamos la app
app = dash.Dash(__name__)
#Layout del dashboard
fig = go.Figure(go.Bar(x=df['Magnitude'].value_counts().index, y=df['Magnitude'].value_counts().values,marker=dict(color='red')))
fig.update_layout(title={'text':'Gráfico de barras magnitud/num de terremotos',
                         'font':{'size':20,'family':'Comic Sans','color':'red'}},
                  xaxis_title='Magnitud',
                  yaxis_title='Número de terremotos')
#Damos formato al titulo y resaltamos el punto mas alto con una anotación
fig.add_annotation(x=2,
                   y=3409,
                   text='Punto más alto',
                   showarrow=True,
                   arrowhead=1,
                   arrowsize=1,
                   arrowwidth=2)
fig2= px.choropleth(locations=df.Country,locationmode='country names',color=df.Magnitude,color_continuous_scale=px.colors.sequential.Plasma)
fig2.update_layout(title='Mapa coroplético de Densidad de Terremotos por Región')
fig3 = go.Figure(go.Scatter(
    x=df.Depth,
    y=df.Magnitude,
    mode='markers',
    marker=dict(color='red',size=10)
))
fig3.update_layout(title='Scatter Plot de Magnitud / Profundidad',
                   xaxis_title='Profundidad',yaxis_title='Magnitud')
app.layout = html.Div(children=[
    html.H1('Información de Terremotos'),
    dcc.Graph(id='grafico-terremotos',figure=fig),
    dcc.Graph(id='Mapa coroplético',figure=fig2),
    dcc.Graph(id='Scatterplot magnitud-densidad',figure=fig3)
      #Insertamos las figuras
])
try:
    if __name__ == '__main__':
        app.run(debug=True) #Ejecutamos el dashboard
except Exception as e:
    print(f"Error: {e}")