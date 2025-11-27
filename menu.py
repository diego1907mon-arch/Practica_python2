from leer import LectorCSV
from Limpieza import Limpieza
from Limpieza1 import Limpieza1
from Limpieza2 import Limpieza2
from estadisticas import Estadisticas
import csv

ruta_entrada = "c:/Users/Aprendiz/Downloads/dataset2_football_matches.csv"
ruta_salida = "c:/Users/Aprendiz/Downloads/dataset2_football_matches_clean.csv"

def limpiar_archivo():
    lector = LectorCSV(ruta_entrada)
    filas = lector.leer()

    fecha = Limpieza()
    na = Limpieza1()
    tex = Limpieza2()

    encabezado = filas[0]
    filas_limpias = []

    for fila in filas[1:]:
        fila[1] = fecha.limpiar_fecha(fila[1])
        fila = [na.limpiar(v) for v in fila]
        fila = [tex.limpiar(v) for v in fila]
        filas_limpias.append(fila)

    with open(ruta_salida, "w", newline="", encoding="utf-8-sig") as f:
        escritor = csv.writer(f)
        escritor.writerow(encabezado)
        escritor.writerows(filas_limpias)

    print("\n✔ Archivo limpio generado correctamente.\n")


