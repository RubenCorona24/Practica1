#--------------------CREAMOS UN DASHBOARD INTERACTIVO CON EL FRAMEWORK DASH-------------------


#Importamos librerías: dash, html,dcc,Input,Output
import pandas as pd
import plotly.express as px
import dash
from dash import html,dcc,Input,Output

#Creamos un dataframe de ejemplo
df = pd.DataFrame({
    'fruta': ['Manzana','Banana','Uvas','Peras','Mango'],
    'cantidad': [166,150,189,176,122],
    'ciudad': ['New York','Bogotá','Ciudad de México','Lima','Washington']
})
#Creamos la app(dash.Dash)
app = dash.Dash(__name__)
#Creamos el layout
fig =px.line(df,x='mes',y='ventas')
app.layout = html.Div(children=[
    html.H1('Ventas Dashboard'),    
    dcc.Dropdown(id='dropdown-mes',
                 options=[{'label':'New York','value':'New York'},
                     {'label':'Bogotá','value':'Bogotá'},
                     {'label':'Ciudad de México','value':'Ciudad de México'},
                     {'label':'Lima','value':'Lima'},
                     {'label':'Washington','value':'Washington'}],
                     value='New York'),
                     dcc.Graph(id='Grafico')
])


#Callbacks para interactividad
@app.callback(
    Output('Grafico','figure'),
    [Input('dropdown-mes','value')]
)
def actualizar_grafico(ciudad):
    df_filtrado = df[df['ciudad'] == ciudad] #Filtramos df
    fig = px.line(df_filtrado,x='fruta',y='cantidad',color='fruta')
    return fig #Devolvemos la figura


#Ejecutamos el Dashboard
try:
    if __name__ == '__main__':
        app.run(debug=True)

except Exception as e:
    print(f"Error: {e}")