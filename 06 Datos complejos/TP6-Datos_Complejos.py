# Trabajo Práctico 6 - Estructuras de datos complejos
# Alumno: Balverdi Nicolás Leonel
# Comisión 25

# Actividad 1
# Dado el diccionario 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios
# Naranja = 1200
# Manzana = 1500
# Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# Actividad 2
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# Actividad 3
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas 
# sin los precios

frutas = list(precios_frutas.keys())

print(frutas)

# Actividad 4
# Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

print("Agendar contactos:")

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")

    contactos[nombre] = numero

buscar = input("Ingrese el nombre del contacto que desea buscar: ")

if buscar in contactos:
    print(f"El número de {buscar} es: {contactos[buscar]}")
else:
    print(f"No hay ningún {buscar} en su lista de contactos")

# Actividad 5
# Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set).
# Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")

palabras = frase.lower().split()
palabrasUnicas = set(palabras)

contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print(f"Las palabras únicas en la frase son: {palabrasUnicas}")
print("Cantidad de veces que aparece cada palabra:")
print(contador_palabras)

# Actividad 6
# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

calificaciones_estudiantes = {}

print("Ingrese el nombre y 3 clasificaciones para el registro de 3 alumnos:")

for i in range(3):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    nota1 = int(input(f"Ingrese la primera nota de {nombre}: "))
    nota2 = int(input(f"Ingrese la segunda nota de {nombre}: "))
    nota3 = int(input(f"Ingrese la tercera nota de {nombre}: "))

    notas = (nota1, nota2, nota3)
    calificaciones_estudiantes[nombre] = notas

for nombre in calificaciones_estudiantes:
    notas = calificaciones_estudiantes[nombre]
    promedio = (notas[0] + notas[1] + notas[2]) / 3
    print(f"El promedio de {nombre} es: {promedio:.2f}")

# Actividad 7
# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)

parcial1 = {"Juan", "Pedro", "Clara", "Ana", "Claudio", "Paula", "Tomas", "Lara", "Lorenzo"}
parcial2 = {"Pedro", "Nicolas", "Paulo", "Claudio", "Ana", "Juan", "Tomas", "Clara", "Paula"}

ambosParciales = parcial1.intersection(parcial2)
unSoloParcial = parcial1.symmetric_difference(parcial2)
alMenosUnParcial = parcial1.union(parcial2)

print(f"Estudiantes que aprobaron ambos parciales: {ambosParciales}")
print(f"Estudiantes que aprobaron un solo parcial: {unSoloParcial}")
print(f"Estudiantes que aprobaron al menos un parcial: {alMenosUnParcial}")

# Actividad 8
# Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe.
# Agregar un nuevo producto si no existe.

# Funciones
def en_stock(prodcuto, registro):
    if prodcuto in registro:
        return True
    else:
        return False

def indicar_stock(producto, registro):
    if en_stock(producto, registro):
        print(registro[producto])
    else:
        print(f"{producto} no se encuentra en stock")

def modificar_stock(producto, registro):
    if en_stock(producto, registro):
        registro[producto] = int(input(f"Modifique el stock de {producto}: "))
        print(f"El stock de {producto} ha sido modificado con exito!")
        print(stock_productos)
    else:
        print(f"El producto {producto} no existe, debe cargarlo seleccionando la operación correcta")

def agregar_producto(producto, registro):
    if not en_stock(producto, registro):
        print(f"Se ha agregado {producto}")
        registro[producto] = int(input(f"Indique la cantidad de unidades de {producto} en stock: "))
        print(stock_productos)
    else:
        print(f"{producto} ya existe en el registro, seleccione la operación correcta para modificarlo")

# Programa principal
stock_productos = {'Xbox Series S' : 5, 'Xbox Series X' : 3, 'PlaySation 5' : 6}

print("== Productos en stock ==")
print("1. Consultar stock")
print("2. Modificar stock")
print("3. Agregar producto")

operacion = int(input("Ingrese el número de la operación que desea realizar: "))
producto = input("Ingrese el producto: ")

if operacion == 1:
    indicar_stock(producto, stock_productos)
elif operacion == 2:
    modificar_stock(producto, stock_productos)
elif operacion == 3:
    agregar_producto(producto, stock_productos)

# Actividad 9
# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

# Funciones
def hay_evento(dia, hora, agenda):
    ocupado = (dia, hora)
    if ocupado in agenda:
        return True
    else:
        return False

def indicar_evento(dia, hora, agenda):
    if hay_evento(dia, hora, agenda):
        ocupado = (dia, hora)
        print(agenda[ocupado])
    else:
        print(f"El día {dia} a las {hora} se encuantra disponible")

# Programa principal

agenda = {
    ("Lunes", "19:00") : "Clase de consulta - Org. Empresarial",
    ("Lunes", "20:00") : "Clase de consulta - Arq. y Sist. Operativos",
    ("Martes", "19:00") : "Clase de consulta - Programación I",
    ("Miércoles", "16:00") : "Clase de consulta - Matemática",
    ("Miércoles", "19:00") : "Clase de consulta - Org. Empresarial",
    ("Miércoles", "20:00") : "Clase de consulta - Arq. y Sist. Operativos",
    ("Viernes", "16:00") : "Clase de consulta - Matemática",
    ("Miércoles", "19:00") : "Clase de consulta - Programación I"
}

print("== Agenda Semanal ==")
print("Para consultar sobre los eventos de la semana, indique: ")
dia = input("Día: ")
hora = input("Horario en formato 24 horas (HH:MM): ")

indicar_evento(dia, hora, agenda)

# Actividad 10
# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores.

paises_y_capitales = {
    "Argentina" : "Ciudad Autonoma de Buenos Aires",
    "Estados Unidos" : "Washington D.C.",
    "Alemania" : "Berlín",
    "China" : "Pekín",
    "Sudáfrica" : "Ciudad del Cabo"
    }

capitales_y_paises = {}

listaPaises = list(paises_y_capitales.keys())

for i in range(len(listaPaises)):
    pais = listaPaises[i]
    capital = paises_y_capitales[pais]
    capitales_y_paises[capital] = pais

print("Diccionario original: ")
print(paises_y_capitales)
print("Diccionario invertido: ")
print(capitales_y_paises)