palabras_unicas = set()
diccionario = {}
entrada = input()

for palabra in entrada.split():
    if palabra not in palabras_unicas:
        palabras_unicas.add(palabras_unicas.add(palabra))

    if palabra in diccionario.keys():
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1

print(palabras_unicas)
print(diccionario)
