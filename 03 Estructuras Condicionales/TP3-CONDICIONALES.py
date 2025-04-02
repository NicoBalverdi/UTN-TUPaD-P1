# Trabajo Practico de Condicionales
# Alumno: Balverdi Nicolás Leonel
# Comisión 25

# Actividad 1
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

edad = int(input("Ingrese su edad: "))

if edad >= 18 :
    print("Es mayor de edad")

# Actividad 2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))

resultado = "Aprobado" if nota >= 6 else "Desaprobado"
print(resultado)

# Actividad 3
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par".

num = int(input("Ingrese un número: "))

if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Actividad 4
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# Niño/a: menor de 12 años.
# Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad >= 0:
    if edad < 12:
        print("Eres niño/a")
    elif edad >= 12 and edad < 18:
        print("Eres adolescente")
    elif edad >= 18 and edad < 30:
        print("Eres adulto/a joven")
    else:
        print("Eres adulto/a")
else:
    print("Ha ingresado un valor menor a 0")

# Actividad 5
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

pw = input("Ingrese una contraseña: ")

if len(pw) >= 8 and len(pw) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Actividad 6
# escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y
# las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import mode, median, mean

randomNumbers = [random.randint(1, 100) for i in range(50)]

media = mean(randomNumbers)
mediana = median(randomNumbers)
moda = mode(randomNumbers)

if media > mediana > moda:
    sesgo = "Sesgo positvo o a la derecha"
elif media < mediana < moda:
    sesgo = "Sesgo negativo o a la izquierda"
else:
    sesgo = "No hay sesgo"

print(f"Lista de números aleatorios {randomNumbers}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Resultado: {sesgo}")

# Actividad 7
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Ingrese una frase: ")

if frase.endswith(("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")):
    frase += "!"

print(frase)

# Actividad 8
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")
print("Seleccione una opción")
print("1. nombre en mayúsculas")
print("2. nombre en minúsculas")
print("3. nombre con primera letra en mayúsculas")
opcion = int(input("Ingrese la opción deseada: "))

if opcion == 1:
    nombre = nombre.upper()
elif opcion == 2:
    nombre = nombre.lower()
else:
    nombre = nombre.title()

print(nombre)

# Actividad 9
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud de un terremoto: "))

if magnitud < 3:
    print("Muy leve e imperceptible")
elif magnitud >= 3 and magnitud < 4:
    print("Leve, ligeramente perceptible")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado, perceptible por pesonas pero generalmente no causan daños")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte, puede causar daños en estructuras débiles")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte, puede causar daños significativos")
else:
    print("Extremo, puede causar graves daños a gran escala")

# Actividad 10
# Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese en qué hemisferio se encuentra, Norte(N) o Sur(S): ")
dia = int(input("Ingrese el día (número): "))
mes = int(input("Ingrese el mes (número): "))

if ((dia >= 21 and mes == 12) or mes == 1 or mes == 2 or (dia <= 20 and mes == 3)) and (hemisferio == "S" or hemisferio == "s"):
    print("Actualmente es verano en el hemisferio seleccionado")
elif ((dia >= 21 and mes == 12) or mes == 1 or mes == 2 or (dia <= 20 and mes == 3)) and (hemisferio == "N" or hemisferio == "n"):
    print("Acutalmente es invierno en el hemisferio seleccionado")
elif ((dia >= 21 and mes == 3) or mes == 4 or mes == 5 or (dia <= 20 and mes == 6)) and (hemisferio == "S" or hemisferio == "s"):
    print("Acutalmente es otoño en el hemisferio seleccionado")
elif ((dia >= 21 and mes == 3) or mes == 4 or mes == 5 or (dia <= 20 and mes == 6)) and (hemisferio == "N" or hemisferio == "n"):
    print("Actualmente es primavera en el hemisferio seleccionado")
elif ((dia >= 21 and mes == 6) or mes == 7 or mes == 8 or (dia <= 20 and mes == 9)) and (hemisferio == "S" or hemisferio == "s"):
    print("Actualmente es invierno en el hemisferio seleccionado")
elif ((dia >= 21 and mes == 6) or mes == 7 or mes == 8 or (dia <= 20 and mes == 9)) and (hemisferio == "N" or hemisferio == "n"):
    print("Acutalmente es verano en el hemisferio seleccionado")
elif ((dia >= 21 and mes == 9) or mes == 10 or mes == 11 or (dia <= 20 and mes == 12)) and (hemisferio == "S" or hemisferio == "s"):
    print("Actualmente es primavera en el hemisferio seleccionado")
elif ((dia >= 21 and mes == 9) or mes == 10 or mes == 11 or (dia <= 20 and mes == 12)) and (hemisferio == "N" or hemisferio == "n"):
    print("Acutalmente es otoño en el hemisferio seleccionado")