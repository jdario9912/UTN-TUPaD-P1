# Ejercicio 1
print("Ejercicio 1")
lista_multiplos_4 = list(range(4,100,4))
print(lista_multiplos_4)
print("")

# Ejercicio 2
print("Ejercicio 2")
mi_lista = ["Honda", True, 501, 6.3, ["A", 2, False]]
print(mi_lista[3])
print(mi_lista[-2])
print("")

# Ejercicio 3
print("Ejercicio 3")
lista_3 = []
lista_3.append("River")
lista_3.append("Mas")
lista_3.append("Grande")
print(lista_3)
print("")

# Ejercicio 4
print("Ejercicio 4")
animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[1] = "loro"
animales[3] = "oso"
print(animales)
print("")

# Ejercicio 5
print("Ejercicio 5")
print("" \
"Se define una lista llamada numeros = [8, 15, 3, 22, 7]\n" \
"En la siguiente linea se buscar el maximo valor dentro de la lista con el metodo max(numeros)\n" \
"El valor devuelto es pasado como argumento al metodo remove que se aplica a la lista numeros: numeros.remove(max(numeros))\n" \
"El resultado es que se elimina el valor 22"
"")
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
print("")

# Ejercicio 6
print("Ejercicio 6")
for i in list(range(10, 31, 5)):
    print(i)
print("")

# Ejercicio 7
print("Ejercicio 7")
autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1] = "207"
autos[2] = "compressor"
print(autos)
print("")

# Ejercicio 8
print("Ejercicio 8")
dobles = []
for i in [5, 10, 15]:
    dobles.append(i*2)
print(dobles)
print("")

# Ejercicio 9
print("Ejercicio 9")
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)
print("")

# Ejercicio 10
print("Ejercicio 10")
lista_anidada = []
lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append([25.5]) 
lista_anidada[2].append(57.9)
lista_anidada[2].append(30.6)
lista_anidada.append(False)
print(lista_anidada)
