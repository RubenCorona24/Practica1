import pandas as pd
import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=RubenSantiago;"
    "DATABASE=Pruebas SQL;"
    "Trusted_Connection=yes;")
df = pd.read_sql("SELECT TOP 10 * FROM Universidades ORDER BY Employment_Rate DESC",conn)
print(df)