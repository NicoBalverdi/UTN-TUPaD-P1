# Definición de funciones
# Actividad 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Actividad 2
def saludar_usuario(user):
    print(f"Hola {user}")

#Actividad 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Actividad 4
from math import pi

def calcular_area_circulo(radio):
    return pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

# Actividad 5
def segundos_a_horas(segundos):
    return segundos / 3600

# Actividad 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} por {i} = {numero * i}")

# Actividad 7
def operaciones_basicas(a, b):
    print(f"El resultado de la suma entre {a} y {b} es {a + b}")
    print(f"El resultado de la resta entre {a} y {b} es {a - b}")
    print(f"El resultado de la multiplicación entre {a} y {b} es {a * b}")
    print(f"El resultado de la división entre {a} y {b} es {a / b}")

# Actividad 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Actividad 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Actividad 10
def  calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
# Actividad 1
imprimir_hola_mundo()

# Actividad 2
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

# Actividad 3
print("Por favor, complete los datos solicitados a continuación")
informacion_personal(input("Nombre: "), input("Apellido: "), int(input("Edad: ")), input("Residencia: ")) # Composición de funciones

# Actividad 4
radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es {calcular_area_circulo(radio)} y su perímetro {calcular_perimetro_circulo(radio)}")

# Actividad 5
segundos = int(input("Ingrese una cantidad de segundos: "))
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas")

# Actividad 6
num = int(input("Ingrese un número: "))
tabla_multiplicar(num)

# Actividad 7
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
operaciones_basicas(num1, num2)

# Actividad 8
metros = float(input("Ingrese su altura en metros: "))
kilogramos = float(input("Ingrese su peso en kilogramos: "))
imc = calcular_imc(kilogramos, metros)
print(f"Su indice de masa corporal es {imc:.2f}")

# Actividad 9
tempC = float(input("Ingrese un temperatura en grados Celsius (°C): "))
tempF = celsius_a_fahrenheit(tempC)
print(f"La temperatura ingresada equivale a {tempF} grados Farenheit (°F)")

# Actividad 10
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))
promedio = calcular_promedio(n1, n2, n3)
print(f"El promedio de {n1}, {n2} y {n3} es {promedio}")