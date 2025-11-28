class Limpieza3:
    def __init__(self):
        self.traducciones = { 
            "match_id": "Id",
            "date": "Fecha",
            "stadium": "Estadio",
            "home_team": "Equipo_local",
            "away_team": "Equipo_visitante",
            "home_goals": "Goles_local",
            "away_goals": "Goles_visitante",
            "yellow_cards": "Tarjetas_amarillas",
            "red_cards": "Tarjetas_rojas",
            "attendance": "Asistencias",
            "tournament": "Torneo"
        }

    def traducir(self, encabezado):
        
        nuevo_titulo = []
        for columna in encabezado:
            nueva = self.traducciones.get(columna, columna)
            nuevo_titulo.append(nueva)
        return nuevo_titulo