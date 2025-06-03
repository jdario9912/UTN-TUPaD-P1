alumnos = {}

cantidad = 3

for alumno in range(cantidad):
    notas = []
    nombre = input("Nombre: ")
    for i in range(cantidad):
        nota = int(input(f"Nota {i + 1}: "))
        notas.append(nota)
    print("")
    alumnos[nombre] = tuple(notas)

promedios = {}

for alumno in alumnos.keys():
    cont = 0
    for nota in list(alumnos[alumno]):
        cont += nota
    promedios[alumno] = {
        "notas": alumnos[alumno],
        "promedio": cont / 3,
    }

print(promedios)
