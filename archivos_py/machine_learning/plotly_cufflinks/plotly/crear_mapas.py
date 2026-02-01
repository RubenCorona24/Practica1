#Podemos crear mapas mediante Scattergeo de plotly.graph_objects y choroplet de plotly.express

#1.- -------------MAPA CON SCATTERGEO----------------
import plotly.graph_objects as go

#Creamos la figura
fig = go.Figure(go.Scattergeo(
    lat=[19.43, 40.71],
    lon=[-99.13,-74.00],
    text=['CDMX','NUEVA YORK'],
    mode='markers',
    marker=dict(size=[16,44,48],color=['red','blue','purple'])
)) #Parámetros: latitud, longitud, texto, modo

fig.update_layout(title="Mapa de Scattergeo New York & Mexico")
fig.show() #MOSTRAMOS LA FIGURA

#ELEMENTOS IMPORTANTES

#-------------------MAPA COROPLÉTICO---------------------------
# permite ver interacciones, cada país tiene color en relación a un valor asignado en cada país

#Importamos libreria plotly.express as px
import plotly.express as px
#Extraemos un dataframe de la misma libreria
df = px.data.gapminder()
df.head() #Vemos los primeros registros del df

# #Creamos una segunda figura donde almacenamos el mapa
fig2 = px.choropleth(df,locations='iso_alpha',
                     color='lifeExp',
                     hover_name='country',
                     color_continuous_scale=px.colors.sequential.Plasma,
                     animation_frame='year') #Recibimos df, locaciones, color en que se basa, escala de color, y animación

fig2.update_layout(title='Mapa Coroplético')
fig2.show() #Mostramos la figura

