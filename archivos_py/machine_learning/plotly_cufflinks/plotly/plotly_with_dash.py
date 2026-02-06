#--------------------CREAMOS UN DASHBOARD INTERACTIVO CON EL FRAMEWORK DASH-------------------


#Importamos librerías: dash, html,dcc,Input,Output
import pandas as pd
import plotly.express as px
import dash
from dash import html,dcc,Input,Output


df = pd.DataFrame({
    'Mes': ['Enero','Febrero'],
    'ventas': [[232,3434,3434],[23243,3443]]
})
#Creamos la app(dash.Dash)
app = dash.Dash(__name__)
#Creamos el layout
app.layout = html.Div([
    html.H1('Ventas Dashboard'),
    dcc.Graph(id='Grafica-ventas'),
    dcc.Dropdown(id='dropwdown-mes',
                 options=[
                     {'label':'Enero','value':'Enero'},
                     {'label':'Febrero','value':'Febrero'}
                 ],
                 value='Enero')
])

#Usamos plotly para graficar en dash
fig =px.line(df,x='Mes',y='ventas')
dcc.Graph(id='Grafica-ventas',figure=fig)

#Callbacks para interactividad
@app.callback(
    Output('Grafica-ventas','figure'),
    Input('dropwdown-mes','value')
)
def actualizar_grafico(mes):
    df_filtrado = df[df['mes'] == mes] #Filtramos df
    px.line(df_filtrado,x='Mes',y='ventas')


#Ejecutamos el Dashboard
try:
    if __name__ == '__main__':
        app.run(debug=True)

except Exception as e:
    print(f"Error: {e}")