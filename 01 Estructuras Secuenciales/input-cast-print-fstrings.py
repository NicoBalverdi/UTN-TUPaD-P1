# print se utiliza para mostrar un mensaje en la pantalla

print("Hola! Vamos a aprender las funciones input y print")

# Usamos la función input para solicitarle un dato o entrada al usuario
# El texto entre parentesis del input se mostrará en pantalla
# En este caso el dato sera almacenado en la variable nombre

nombre = input("Por favor ingresa tu nombre: ")

# Ahora saludaremos al usuario concatenando la variable nombre en la función print

print("Mucho gusto, " + nombre + "!")

# Procedemos a solicitarle la edad a nuestro usuario
# Esta vez almacenaremos la entrada en la variable edad

edad = input(nombre + ", ingresa tu edad por favor: ")

# Dado que input por defecto define las entradas como strings si necesitamos que el valor almacenado en la variable sea otro
# Debemos realizar una conversión
# En este ejemplo haremos que el dato almacenado en edad sea un entero utilizando int()

edad = int(edad)

# Para comprobar que el contenido de la variable ahora es un valor de tipo entero le solicitaremos al usuario otro número
# Esta vez queremos un decimal y realizaremos su conversion con con float()
# Luego sumaremos los valores y los mostraremos por pantalla

num = input(nombre + ", ingresa un número decimal: ")
num = float(num)
suma = edad + num

# Al momento de mostrar por pantalla es importante tener en cuenta que no podremos concatenar datos numericos usando "+"
# Debemos utilizar la coma ","
print(nombre + ", el resultado de la suma de tu edad y el número decimal ingresado es :", suma)

# Podemos utilizar f strings para mostrar en pantallas cadenas de una forma más sencilla evitando "+" y ","
# Tambien pueden ser utilizados en inputs y variables donde haya cadenas!
# Para utilizarlo debemos anteponer la letra f a las comillas de nuestra cadena

print(f"A continuación te mostrare los datos ingresados {nombre}")
apellido = input(f"Aun no me has dicho tu apellido {nombre}: ")
print(f"Tu nombre es {nombre}, tu edad es {edad}, el número decimal es {num} y tu apellido es {apellido}")
saludo = f"Eso es todo {nombre} {apellido}, espero que te hayas divertido!"
print(saludo)