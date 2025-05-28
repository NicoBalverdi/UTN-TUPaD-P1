# Trabajo Práctico - Recursividad
# Alumno: Balverdi Nicolás Leonel
# Comisión 25

import sys
sys.setrecursionlimit(20000)

# Funciones

# Actividad 1
def factorialDeN(n):
    if n == 0:
        return 1
    else:
        return n * factorialDeN(n - 1)

# Actividad 2
def fibonacciRecur(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacciRecur(posicion - 1) + fibonacciRecur(posicion - 2)

# Actividad 3
def potenciaRecur(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potenciaRecur(base, exponente - 1)

# Actividad 4
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Actividad 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Actividad 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Actividad 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Actividad 8
def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        coincidencia = 1 if (numero % 10) == digito else 0
        return coincidencia + contar_digito(numero // 10, digito)

# Programa Principal

# Actividad 1

print("== Calcular el factorial de números comprendidos entre 1 y un número determinado ==")
limite = int(input("Ingrese un número: "))

for i in range(1, limite + 1):
    print(f"El factorial de {i} es {factorialDeN(i)}")

# Actividad 2
print("== Mostrar la serie Fibonacci hasta una posición determinada ==")
p = int(input("Ingrese un número para determinar una posición en la serie: "))

for i in range(0, p + 1):
    print(f"El valor de la posición {i} en la serie es {fibonacciRecur(i)}")

# Actividad 3
print("== Calcular potencia de manera recursiva ==")
base = int(input("Ingrese un número: "))
exponente = int(input("Ingrese el exponente: "))

print(f"El resultado es: {potenciaRecur(base, exponente)}")

# Actividad 4
print("== Pasar un número de base decimal a binario de manera recursiva ==")
n = int(input("Ingrese un número de base 10 positivo: "))
if n == 0:
    print("El 0 se representa de la misma manera en binario.")
else:
    print(f"El {n} se representa como {decimal_a_binario(n)} en binario.")

# Actividad 5
print("== Detector de palíndromos ==")
palabra = input("Ingrese una palabra sin espacios ni tildes: ")
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")

# Actividad 6
print("== Sumando dígitos de un número de manera recursiva ==")
num = int(input("Ingrese un número: "))
print(f"La suma de los dígitos de {num} es: {suma_digitos(num)}")

# Actividad 7
print("== Contar los bloques de una pirámide de forma recursiva ==")
bloques = int(input("Indique la cantidad de bloques en la base de la pirámide: "))
print(f"Se necesitan {contar_bloques(bloques)} bloques para armar la pirámide")

# Actividad 8
print("== Contar cuántas veces se repite un dígito en un número dado ==")
num = int(input("Ingrese un número: "))
digito = int(input("Ingrese el dígito: "))
print(f"El dígito {digito} se repite {contar_digito(num, digito)} veces en el número {num}")