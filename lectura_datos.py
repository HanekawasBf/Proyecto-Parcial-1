import pandas as pd

def leer_muestras(ruta_archivo):
    datos = pd.read_csv(ruta_archivo)
    return datos["x"].tolist(), datos["y"].tolist()