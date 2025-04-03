# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

# Periodo del año                           Estación en elhemisferio norte   Estación en el hemisferio sur
# Desde el 21 de diciembre hasta el 20 de
# marzo (incluidos)                               Invierno                            Verano
# Desde el 21 de marzo hasta el 20 de junio
# (incluidos)                                     Primavera                             Otoño
# Desde el 21 de junio hasta el 20 de
# septiembre (incluidos)                          Verano                               Invierno
# Desde el 21 de septiembre hasta el 20 de
# diciembre (incluidos)                           Otoño                                Primavera

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingresa el hemisferio (N/S): ")
mes = input("Ingresa el mes (nombre): ")
dia = int(input("Ingresa el dia del mes(numero): "))

if mes == "enero" or mes == "febrero" or (mes == "diciembre" and dia >= 21) or (mes == "marzo" and dia <= 20):
    if hemisferio == "S":
        print("Verano")
    elif hemisferio == "N":
        print("Invierno")
elif mes == "abril" or mes == "mayo" or (mes == "marzo" and dia >= 21) or (mes == "junio" and dia <= 20):
    if hemisferio == "S":
        print("Otoño")
    elif hemisferio == "N":
        print("Primavera")
elif mes == "julio" or mes == "agosto" or (mes == "junio" and dia >= 21) or (mes == "septiembre" and dia <= 20):
    if hemisferio == "S":
        print("Invierno")
    elif hemisferio == "N":
        print("Verano")
elif mes == "octubre" or mes == "noviembre" or (mes == "septiembre" and dia >= 21) or (mes == "diciembre" and dia <= 20):
    if hemisferio == "S":
        print("Primavera")
    elif hemisferio == "N":
        print("Otoño")
else:
    pass