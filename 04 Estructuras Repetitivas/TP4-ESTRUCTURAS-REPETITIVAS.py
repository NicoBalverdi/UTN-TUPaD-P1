#Alumno: Balverdi Nicolás Leonel
#Comisión 25

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#   (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for cont in range(0, 101):
    print(cont)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#   dígitos que contiene.

num = int(input("Ingrese un número entero: "))

valorInicial = num
cont = 0

num = abs(num)

if num > 0:
    while num > 0:
        num = num // 10
        cont += 1
elif num == 0:
    cont = 1

print(f"La cantidad de cifras que tiene {valorInicial} es {cont}")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#   dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))
sum = 0

if num1 < num2:
    for valor in range(num1+1, num2):
        sum += valor
elif num2 < num1:
    for valor in range(num2+1, num1):
        sum += valor

print(f"El resultado de la sumatoria de los valores comprendidos entre {num1} y {num2} es {sum}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#   secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#   un 0.

CORTE = 0

num = int(input(f"Ingrese el número entero que desea sumar ({CORTE} para terminar): "))
sum = 0

while num != 0:
    sum += num
    num = int(input(f"Ingrese otro número entero para sumar ({CORTE} para terminar): "))

print(f"La sumatoria de los valores ingresados es {sum}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#   programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numRandom = random.randint(0, 9)

numUser = int(input("Intente adivinar el número entero aleatorio entre 0 y 9: "))
cont = 0

while numUser != numRandom:
    numUser = int(input("Incorrecto, intente nuevamente: "))
    cont += 1

if cont == 0:
    cont = 1
    print(f"Felicidades, has acertado luego de {cont} intento!")
else:
    print(f"Muy bien, has acertado luego de {cont} intentos!")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#   entre 0 y 100, en orden decreciente.

for cont in range(100, -1, -1):
    print(cont)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#   número entero positivo indicado por el usuario.

num = int(input("Indique un número: "))
sum = 0

if num >= 0:
    for valor in range(0, num+1):
        sum += valor
else:
    for valor in range(0, num-1, -1):
        sum += valor

print(f"La sume de todos los números comprendidos entre 0 y {num} es {sum}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#   programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#   negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#   menor, pero debe estar preparado para procesar 100 números con un solo cambio).

CANTIDAD_INGRESOS = 5

pares = 0
impares = 0
negativos = 0
positvos = 0

for cont in range(1, CANTIDAD_INGRESOS+1):
    num = int(input(f"Ingrese el {cont} de {CANTIDAD_INGRESOS} números enteros: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if num < 0:
        negativos += 1
    else:
        positvos += 1

print(f"La cantidad de números pares ingresados es: {pares}\nLa cantidad de números impares ingresados es: {impares}")
print(f"La cantidad de números positivos ingresados es: {positvos}\nLa cantidad de números negativos ingresados es: {negativos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#   media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#   poder procesar 100 números cambiando solo un valor).

CANTIDAD_INGRESOS = 5
acu = 0

for cont in range(1, CANTIDAD_INGRESOS+1):
    num = int(input(f"Ingrese el {cont} de {CANTIDAD_INGRESOS} números enteros: "))
    acu += num

promedio = acu / cont

print(f"La media de los números ingresados es: {promedio}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#    usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input(f"Ingrese un número entero: "))
valorInicial = num
num = abs(num)
numInvertido = 0

while num > 0:
    digito = num % 10
    numInvertido = numInvertido * 10 + digito
    num = num // 10

if valorInicial < 0:
    numInvertido *= -1
    print(f"{valorInicial} al revés es: {numInvertido}")
else:
    print(f"{valorInicial} al revés es: {numInvertido}")