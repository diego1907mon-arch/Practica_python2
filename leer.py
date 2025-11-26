import csv

class LectorCSV:
    def __init__(self,ruta):
        self.ruta=ruta

    def leer(self):
        with open(self.ruta,newline='',encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                print(fila)

ruta_csv="c:/Users/Aprendiz/Downloads/dataset2_football_matches.csv"
lector=LectorCSV(ruta_csv)
lector.leer()