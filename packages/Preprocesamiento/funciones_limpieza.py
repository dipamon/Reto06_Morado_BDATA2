import os
import pickle
import pandas as pd


def leer_datos(nombre_archivo, origen):
    if origen.lower() in ['org', 'originales']:
        ruta_datos = os.path.join('..', 'Datos', 'Originales')
    elif origen.lower() in ['trf', 'transformados']:
        ruta_datos = os.path.join('..', 'Datos', 'Transformados')
    else:
        print('El parámetro "origen" no está bien especificado')
        return None
    
    ruta_archivo = os.path.join(ruta_datos, nombre_archivo)
    return pd.read_csv(ruta_archivo, index_col = [0])


def guardar_objeto(obj, nombre, destino):
    if destino.lower() in ['org', 'originales']:
        destino = 'Originales'
    elif destino.lower() in ['trf', 'transformados']:
        destino = 'Transformados'
    else:
        print('El parámetro "destino" no está bien especificado')
        return None
    
    nombre_extension = f'{nombre}.pkl'
    with open(os.path.join('..', 'Datos', destino, nombre_extension), 'wb') as f:
        pickle.dump(obj, f)
    
    return

def cargar_objeto(nombre, origen):
    if origen.lower() in ['org', 'originales']:
        origen = 'Originales'
    elif origen.lower() in ['trf', 'transformados']:
        origen = 'Transformados'
    else:
        print('El parámetro "origen" no está bien especificado')
        return None
    
    nombre_extension = f'{nombre}.pkl'
    with open(os.path.join('..', 'Datos', origen, nombre_extension), 'rb') as f:
        objeto_cargado = pickle.load(f)
    
    return objeto_cargado