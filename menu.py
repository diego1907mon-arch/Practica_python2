from estadisticas import EstadisticasEquipos

class Menu:
    def __init__(self, ruta_csv):
        self.est = EstadisticasEquipos(ruta_csv)

    def mostrar_menu(self):
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver equipos disponibles")
        print("2. Ver estadísticas de un equipo")
        print("3. Salir")

    def mostrar_equipos(self):
        print("\n--- EQUIPOS DISPONIBLES ---")
        equipos = self.est.equipos_disponibles()

        for i, equipo in enumerate(equipos, 1):
            print(f"{i}. {equipo}")

        return equipos

    def seleccionar_equipo(self):
        equipos = self.mostrar_equipos()

        try:
            opcion = int(input("\nSeleccione un equipo por número: "))
            if opcion < 1 or opcion > len(equipos):
                print("❌ Opción inválida.")
                return None
            return equipos[opcion - 1]
        except ValueError:
            print("❌ Debe ingresar un número.")
            return None

    def iniciar(self):
        while True:
            self.mostrar_menu()
            opc = input("\nIngrese opción: ")

            if opc == "1":
                self.mostrar_equipos()

            elif opc == "2":
                equipo = self.seleccionar_equipo()
                if equipo:
                    stats = self.est.estadisticas_equipo(equipo)

                    print(f"\n--- ESTADÍSTICAS DE {equipo} ---")
                    for k, v in stats.items():
                        print(f"{k}: {v}")

            elif opc == "3":
                print("Saliendo del programa...")
                break

            else:
                print("❌ Opción no válida.")


# Ejecutar menú
if __name__ == "__main__":
    ruta =  "c:/Users/Aprendiz/Downloads/dataset2_football_matches_clean.csv"
    menu = Menu(ruta)
    menu.iniciar()


