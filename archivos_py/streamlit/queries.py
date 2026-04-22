import pandas as pd
import pyodbc
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=RubenSantiago;"
    "DATABASE=Pruebas SQL;"
    "Trusted_Connection=yes;")
df = pd.read_sql("SELECT * FROM dataset_oscars",conn) 

#Compositores con más premios
q1 = "SELECT TOP 10 Composer,count(*) AS Premios FROM dataset_oscars GROUP BY Composer ORDER BY Premios DESC"
top_compositores = pd.read_sql(q1,conn)

#Premios por año
q2 = "SELECT Year,COUNT(*) AS Premios FROM dataset_oscars GROUP BY Year ORDER BY Year ASC"
premios_anio = pd.read_sql(q2,conn)

q3 = "SELECT TOP 1 Composer, COUNT(*) AS TotalPremios FROM dataset_oscars GROUP BY Composer ORDER BY TotalPremios DESC"
compositor_exitoso = pd.read_sql(q3,conn)

def datos():
    return df,top_compositores,premios_anio,compositor_exitoso #Devolvemos datos