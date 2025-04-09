import random

count = 0
numero_aleatorio = random.randint(0, 9)

print("Adivinar un numero entre 0 y 9")

while True:
    num = int(input("Tu numero: "))
    count = count + 1
    if num == numero_aleatorio:
        break
    else:
        print("Fallaste, intentar otra vez...")
print("")
print(f"El numero era {numero_aleatorio}")
print(f"Intentos: {count}")
    