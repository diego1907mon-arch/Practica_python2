import csv

class Estadisticas:
    def __init__(self, ruta):
        self.ruta = ruta
        self.datos = []
        self.encabezado = []

    def cargar(self):
        with open(self.ruta, encoding="utf-8-sig") as f:
            lector = csv.reader(f)
            filas = list(lector)
            self.encabezado = filas[0]
            self.datos = filas[1:]

