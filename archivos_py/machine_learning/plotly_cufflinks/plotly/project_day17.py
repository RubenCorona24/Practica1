#-------------DISEÑAMOS UN DASHBOARD EN BASE A DATOS DE TERREMOTO OFICIALES----------------
import pandas as pd
import plotly.graph_objects as go
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
                  xaxis_title='Números',
                  yaxis_title='Magnitud',)
#Damos formato al titulo y resaltamos el punto mas alto con una anotación
fig.add_annotation(x=2,
                   y=3409,
                   text='Punto más alto',
                   showarrow=True,
                   arrowhead=1,
                   arrowsize=1,
                   arrowwidth=2)
app.layout = html.Div(children=[
    html.H1('Información de Terremotos'),
    dcc.Graph(id='grafico-terremotos',figure=fig) #Insertamos la figura
])
try:
    if __name__ == '__main__':
        app.run(debug=True) #Ejecutamos el dashboard
except Exception as e:
    print(f"Error: {e}")