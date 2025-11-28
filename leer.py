
import csv
class LectorCSV:
    def _init_(self, ruta):
        self.ruta = ruta

    def leer(self):  # <- esto debe estar indentado dentro de la clase
        filas = []
        with open(self.ruta, newline='', encoding='utf-8-sig') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                filas.append(fila)
        return filas 