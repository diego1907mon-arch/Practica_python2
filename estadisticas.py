import csv

class EstadisticasEquipos:
    def __init__(self, ruta_csv):
        self.ruta = ruta_csv
        self.partidos = self.cargar_partidos()

    def cargar_partidos(self):
        with open(self.ruta, encoding="utf-8-sig") as f:
            lector = csv.DictReader(f)
            return list(lector)

    def equipos_disponibles(self):
        equipos = set()
        for fila in self.partidos:
            equipos.add(fila["Equipo_local"])
            equipos.add(fila["Equipo_visitante"])
        return sorted(equipos)

    def estadisticas_equipo(self, equipo):
        pj = v = e = d = gf = gc = 0

        for fila in self.partidos:
            local = fila["Equipo_local"]
            visita = fila["Equipo_visitante"]
            gl = int(fila["Goles_local"])
            gv = int(fila["Goles_visitante"])

            if equipo == local:
                pj += 1
                gf += gl
                gc += gv

                if gl > gv: v += 1
                elif gl == gv: e += 1
                else: d += 1

            elif equipo == visita:
                pj += 1
                gf += gv
                gc += gl

                if gv > gl: v += 1
                elif gv == gl: e += 1
                else: d += 1

        dg = gf - gc
        prom_goles = gf / pj if pj > 0 else 0

        return {
            "Partidos jugados ": pj,
            "Victorias ": v,
            "Empates": e,
            "Derrotas": d,
            "Goles a favor": gf,
            "Goles en contra": gc,
            "Diferencia de gol": dg,
            "Promedio_goles": round(prom_goles, 2)
        }

