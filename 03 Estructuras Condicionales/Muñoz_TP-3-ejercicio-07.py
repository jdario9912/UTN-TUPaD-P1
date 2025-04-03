frase = input("Ingresa una frase o palabra: ")

ultima_letra = frase[len(frase)-1]

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{frase}!")
else:
    print(frase)