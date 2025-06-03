contactos = {}
cantidad = 5
print(f"Ingresa {cantidad} contactos con sus numeros.")
for i in range(cantidad + 1):
    # print(f"{i + 1}")
    nombre = input(f"{i + 1}\nNombre: ")
    numero = input("Numero: ")
    print("--------------------------\n")

    contactos[nombre] = numero

buscar = input("Buscar: ")

if contactos[buscar]:
    print(f"Nombre: {buscar}\nNumero: {contactos[buscar]}")
else:
    print(f"El contacto {buscar} no esta registrado.")
