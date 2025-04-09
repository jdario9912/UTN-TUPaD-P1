import math

num = int(input("Ingresa un numero entero: "))

count = 0

while num != 0:
    count = count + 1
    num = num / 10
    num = math.trunc(num)
    
print(count)