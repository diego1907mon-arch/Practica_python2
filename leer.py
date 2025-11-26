import csv


def leer_csv(ruta):
    filas=[]
    with open(ruta, encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            filas.append(fila)
    return filas
        
archivo = "c:/Users/Aprendiz/Downloads/dataset2_football_matches.csv"
datos = leer_csv(archivo)

print("cantidad de datos:",len(datos))