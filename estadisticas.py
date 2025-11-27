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

    def es_numerico(self, valor):
        try:
            float(valor)
            return True
        except:
            return False

    def columnas_numericas(self):
        numericas = []
        for i, col in enumerate(self.encabezado):
            if all(self.es_numerico(fila[i]) for fila in self.datos if fila[i] != ""):
                numericas.append(i)
        return numericas

    def generar(self):
        self.cargar()

        total_filas = len(self.datos)
        col_nums = self.columnas_numericas()
        resumen = {}

        for i in col_nums:
            valores = [float(fila[i]) for fila in self.datos if fila[i] != ""]
            resumen[self.encabezado[i]] = {
                "suma": sum(valores),
                "promedio": sum(valores) / len(valores) if valores else 0,
                "mínimo": min(valores),
                "máximo": max(valores),
                "cantidad ceros": valores.count(0)
            }

        return {
            "filas_totales": total_filas,
            "columnas_numericas": [self.encabezado[i] for i in col_nums],
            "resumen": resumen
        }