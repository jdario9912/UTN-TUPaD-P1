eventos = {}
opcion = -1

while not opcion == "0":
    opcion = input(f"1. Crear evento en la agenda\n2. Consultar agenda\n0. Salir\n")
    print("")

    if opcion == "1":
        dia = input("Dia: ")
        hora = input("Hora: ")
        evento = input("Evento: ")
        eventos[(dia, hora)] = evento
        print("\n")
    if opcion == "2":
        coincidencia = False

        for clave in list(eventos.keys()):
            if list(clave)[0] == dia and list(clave)[1] == hora:
                coincidencia = True
                break

        if coincidencia:
            print(f"\n{hora} {dia} -> {eventos[(dia, hora)]}\n")
        else:
            print(f"No hay eventos el {dia} a las {hora}\n")
