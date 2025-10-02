import pandas as pd
#Leemos el archivo xlsx
def leer_archivo():
    try:
        df = pd.read_csv("archivos_aparte/Datos_Ventas_Tienda2.csv")
        return df
    except:
        print("ERROR, ARCHIVO NO ENCONTRADO")
df = leer_archivo()

def examinar_df(df):
    try:
        first = df.head()
        tail = df.tail()
        forma = df.shape
        valores_nulos = df.isnull().sum()
        print("Información del DataFrame")
        df.info()
        print(f"\n\nPrimeras columnas:\n{first}\n\nÚltimas columnas:\n{tail}\n\nForm:\n{forma}\n\nNulos:\n{valores_nulos}")
    except:
        print("ERROR EN EL ARCHVIO O DE SINTAXIS")
    finally:
        print("Examinación del DataFrame completado")

def limpiar_datos(df):
    if df.isnull().sum().sum() ==0:
        print("No hay datos por limpiar")
        return df
    else:
        df_limpio = df.dropna()
        print("Valores Limpios Ejecutados")
        return df_limpio

def ordenar_values(df):
    try:
        print(f"Este es tu DataFrame:{df}")
        ordenación = input("Columna ordenada: ")
        df_ordenado = df.sort_values(by=ordenación,ascending=False)
        print("Prdenaciópn exitosa")
        return df_ordenado
    except Exception as e:
        print(f"Error al ordenar: {e}")
        return df
    finally:
        print("----Ordenación de DataFrame finalizada-----")

def guardar_df(df):
    df.to_csv("archivos_aparte/New_data.csv")
    print("Datos guardados correctamente")

def menu(df):
    print("----BIENVENIDO A LA MANIPULACIÓN DE DATAFRAMES------")
    print(f"Tu Dataframe:\n{df}")
    while True:
        opcion = int(input("Elige una de las opciones para tu Dataframe:\n1:Examinar df\n2:Limpiar_datos\n3:Ordenar Valores\n4:Guardar Dataframe\n5:Salir\n: "))
        if opcion == 1:
            examinar_df(df)
            continue
        elif opcion ==2:
            df = limpiar_datos(df)
            continue
        elif opcion ==3:
            df = ordenar_values(df)
            continue
        elif opcion ==4:
            guardar_df(df)
            continue
        elif opcion==5:
            print("Muchas gracias por tu atención!!")
            break
        else:
            print("No Elegiste Ninguna opción")
            continue


df = leer_archivo()
if df is not None:
    df=menu(df)


    




