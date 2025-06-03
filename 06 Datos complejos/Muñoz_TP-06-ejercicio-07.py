# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# •Mostrá los que aprobaron ambos parciales.
# •Mostrá los que aprobaron solo uno de los dos.
# •Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {1, 2, 3, 4, 5, 6}
parcial_2 = {5, 6, 7, 8, 9, 10}

# Estudiantes que aprobaron ambos parciales
aprobados_ambos = parcial_1.intersection(parcial_2)
print("Aprobados en ambos parciales:", aprobados_ambos)
# Estudiantes que aprobaron solo uno de los dos
aprobados_solo_uno = parcial_1.symmetric_difference(parcial_2)
print("Aprobados solo en uno de los parciales:", aprobados_solo_uno)
# Lista total de estudiantes que aprobaron al menos un parcial (sin repetir)
aprobados_total = parcial_1.union(parcial_2)
print("Total de aprobados al menos un parcial:", aprobados_total)
