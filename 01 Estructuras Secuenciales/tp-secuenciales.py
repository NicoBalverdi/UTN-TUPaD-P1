# TP Estructuras Secuenciales - Balverdi Nicolás Leonel

# Actividad 1
print("Hola Mundo!")

# Actividad 2
nombre = input("Por favor, ingrese su nombre: ")
print(f"Hola {nombre}!")

# Actividad 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugarResidencia = input("Indique su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarResidencia}")

# Actividad 4
radio = float(input("Ingrese el radio del circulo: "))
pi = 3.1416
area = pi * radio**2
perimetro = 2 * pi * radio
print(f"El área del circulo es {area} y su perímetro es {perimetro}")

# Actividad 5
segundos = int(input("Ingrese una cantidad aleatoria de segundos: "))
horas = segundos / 60
print(f"La cantidad de sgundos ingresada equivale a {horas} horas")

# Actividad 6
num = int(input("Ingrese un número para conocer su tabla de multiplicar: "))
print(f"{num} x 1 = {num}")
print(f"{num} x 2 = {num * 2}")
print(f"{num} x 3 = {num * 3}")
print(f"{num} x 4 = {num * 4}")
print(f"{num} x 5 = {num * 5}")
print(f"{num} x 6 = {num * 6}")
print(f"{num} x 7 = {num * 7}")
print(f"{num} x 8 = {num * 8}")
print(f"{num} x 9 = {num * 9}")
print(f"{num} x 10 = {num * 10}")

# Actividad 7
num = int(input("Ingrese un número distinto de cero (0): "))
num2 = int(input("Ingrese un segundo número distinto de cero (0): "))
if num != 0 and num2 != 0:
    print(f"El resultado de la suma entre {num} y {num2} es {num + num2}")
    print(f"El resultado de dividir {num} por {num2} es {num / num2}")
    print(f"El resultado de multiplicar {num} por {num2} es {num * num2}")
    print(f"El resultado de restarle {num2} a {num} es {num - num2}")
else:
    print("Alguno de los valores ingresados es 0")

# Actividad 8
peso = float(input("Ingrese su peso en Kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / altura**2
print(f"Su indice de masa corporal es {imc}")

# Actividad 9
tempC = float(input("Ingrese una temperatura en grados Celsius: "))
tempF = 9/5 * tempC + 32
print(f"El equivalente de {tempC} en grados Fahrenheit es {tempF}")

#Actividad 10
num = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un segundo número: "))
num3 = int(input("Ingrese el último número: "))
promedio = (num + num2 + num3) / 3
print(f"El promedio es {promedio}")