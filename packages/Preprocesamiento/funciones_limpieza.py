import os
import pandas as pd


def leer_datos(nombre_archivo, origen):
    if origen.lower() in ['org', 'originales']:
        ruta_datos = os.path.join('..\\Datos', 'Originales')
    elif origen.lower() in ['trf', 'transformados']:
        ruta_datos = os.path.join('..\\Datos', 'Transformados')
    else:
        print('El parámetro "origen" no está bien especificado')
        return None
    
    ruta_archivo = os.path.join(ruta_datos, nombre_archivo)
    return pd.read_csv(ruta_archivo, index_col = [0])

def remove_column(df, colnames):
    return df.drop(columns=colnames)

def remove_rows_with_nas(df, colnames):
    return df[df[colnames].notna()]

def save_clean_data(df, file):
    df.to_csv(file)
    return None