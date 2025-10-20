import pandas as pd
import matplotlib.pyplot as plt
#Leemos un archivo csv con pandas
try:
    df = pd.read_csv("archivos_aparte/Datos+Meteorológicos_Arg_2023.csv")
except:
    print("NO SE PUDO LEER EL ARCHIVO")

def pripiedades_dataframe(data):
    print(f"Forma del DF: {data.shape}\n")
    data.info
    print(data.describe())


def verificar_nulos(df):
    nulos = df.isnull().sum()
    print(f"Valores nulos:\n{nulos} ")

def ordenar_valores(df):
    column = input("Columna a ordenar: ")
    new = df.sort_values(by=column,ascending=False)
    print(f"Nueva data con columna {column} ordenados:\n{new.head(5)}")
    
def agrupar_datos(df):
    datos = input("Que datos quieres agrupar?: ")
    valores = input("Que valores quieres hacer el cálculo?: ") 
    pass

def graficar(df):
    type_graf = input("Tipo de gráfica: ")
    plt.style.use("dark_background")
    if type_graf in ['plot','bar','scatter','hist']:
        if type_graf == 'plot':
            column_x = input("Eje x: ")
            column_y = input("Eje y: ")
            fig, ax = plt.subplots()
            ax.plot(df[column_x],df[column_y])
            plt.title(f"DATOS EJE X: {column_x}, EJE Y: {column_y}")
            plt.xlabel(f"{column_x}")
            plt.ylabel(f"{column_y}")
            plt.show()
        elif type_graf == 'bar':
            column_x = input("Eje x: ")
            column_y = input("Eje y: ")
            fig, ax = plt.subplots()
            ax.bar(df[column_x],df[column_y])
            plt.title(f"DATOS EJE X: {column_x}, EJE Y: {column_y}")
            plt.xlabel(f"{column_x}")
            plt.ylabel(f"{column_y}")
            plt.show()
            plt.show()
        elif type_graf =='scatter':
            column_x = input("Eje x: ")
            column_y = input("Eje y: ")
            fig, ax = plt.subplots()
            ax.scatter(df[column_x],df[column_y])
            plt.title(f"DATOS EJE X: {column_x}, EJE Y: {column_y}")
            plt.xlabel(f"{column_x}")
            plt.ylabel(f"{column_y}")
            plt.show()
            plt.show()
        elif type_graf =='hist':
            column_x = input("Eje x: ")
            column_y = input("Eje y: ")
            fig, ax = plt.subplots()
            ax.hist(df[column_x],df[column_y])
            plt.show()
    else:                       
        print("ERROR, NO DISPONEMOS DE ESE TIPO DE GRÁFICO")
    

#Asegurar que las fechas estén en el formato correcto
#Cambiar a tipo de fecha
#Programa que pida al usuario seleccionar una ciudad, de la lista de ciudades disponibles en nuestro df, y un mes
#Gráfico de temperaturas minimas y máximas que se registraron en la ciudad con el mes elegido
def graficar_ciudad_mes():
    #modificamos columna fecha
    df['Fecha'] = pd.to_datetime(df['Fecha'],dayfirst=True, errors='coerce')
    city = input(f"Seleccione la ciudad entre la siguiente lista:\n{df['Ciudad']}\nSelección: ")
    month = int(input("Seleccione un mes en número: "))
    print(f"Vamos a graficar con lo siguientes datos:\nCiudad: {city}\nMes: {month}")
    filtro = (df['Ciudad'] == city)  & (df['Fecha'].dt.month  == month)
    df_filtrado = df.loc[filtro]
    plt.style.use("dark_background")
    fig, ax = plt.subplots()
    
    plt.plot(df_filtrado['Fecha'],df_filtrado['Temperatura Maxima'],marker='o',color='red',label='Temperatura Máxima')
    plt.plot(df_filtrado['Fecha'],df_filtrado['Temperatura Minima'],marker='o',color='white',label='Temperatura Mínima')
    plt.title(f"Temperaturas de ciudad {city} del mes {month}")
    plt.xlabel("Fecha")
    plt.ylabel("Temperatura Celsius ")
    plt.legend()
    plt.grid(True)
    plt.show()
print("-------BIENVENIDO AL GRAFICADOR DE DATOS EN COMUNIDADES-------")
#Hacer el bucle
while True:
    eleccion = int(input("Seleccione entre las siguientes opciones:\n1: Visualizar el DataFrame\n2: Graficación personalizada\n3: GRaficar temp máxima/mínima de ciudad\n4: Salir\nSelección: "))
    if eleccion ==1:
        print(f"Visualizar el DataFrame:\n{df}\nPrimeros datos:{df.head(10)}\nÚltimos datos:{df.tail(10)}")
        continue
    elif eleccion ==2:
        print(f"----GRAFICACIÓN PERSONALIZADA------")
        graficar(df)
        continue
    elif eleccion ==3:
        print("----GRAFICAR TEMP MÁXIMA/MÍNIMA------")
        graficar_ciudad_mes()
        continue
    elif eleccion==4:
        print("Muchas gracias por tu preferencia, mantente informado!!")
        break