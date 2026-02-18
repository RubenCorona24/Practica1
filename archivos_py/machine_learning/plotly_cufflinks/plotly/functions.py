import pandas as pd

def visualize(df):
    nulls = df.isnull().sum()
    print(f"Valores nulos: {nulls}")
    print(f"\nInfo. del DF:\n{df.info} ")
    print(f"\nDescripción del DF:\n{df.describe}")
    print(f"\nPrimeros registros del DF:\n{df.head()}")
    print(f"\nÚltimos registros del DF:\n{df.tail()}")


def clean_df(df):
        df_cleaned = df.dropna()
        df_cleaned = df_cleaned.drop_duplicates()
        return df_cleaned