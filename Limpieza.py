class Limpieza:
    def limpiar_fecha(self, fecha):
        dia, mes, año = fecha.split("/")
        return f"{año}-{mes}-{dia}"
    

    
