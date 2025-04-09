acc = 0

while True:
    num = int(input("Ingresa un numero entero: "))
    if num == 0:
        break
    acc = acc + num

print(f"Total: {acc}")