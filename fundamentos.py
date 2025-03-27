# diferentes strings 
name = "David" 
name_2 = 'David'
name_3 = """David
Orlando""" # se puede usar para escribir un parrafo

print(name)
print(name_2)
print(name_3)

# Ejemplos de f-strings
nombre = "Ana"
edad = 25
print(f"Me llamo {nombre} y tengo {edad} años") # f-string permite insertar variables usando {}
print("Me llamo " + nombre + " y tengo " + str(edad) + " años") # forma tradicional sin f-string

# 2. Naming y declaración de variables
# Variables con nombres descriptivos
nombre_usuario = "Juan"
edad = 25
altura = 1.75
es_activo = True

# 3. Format y f-strings
def ejemplo_format():
    # Usando .format()
    nombre = "María"
    edad = 30
    print("Hola, me llamo {} y tengo {} años".format(nombre, edad))
    
    # Usando f-strings (más moderno)
    print(f"Hola, me llamo {nombre} y tengo {edad} años")
    
    # F-strings con expresiones
    precio = 99.99
    iva = 0.21
    print(f"El precio con IVA es: {precio * (1 + iva):.2f}€")

ejemplo_format()







# --------------- TIPOS DATOS ----------------------

def ejemplos_tipos_datos():

    # Numeros enteros (int)
    x = 10
    print(type(x))
    # Numeros decimales (float)
    y = 10.5
    print(type(y))

    # Cadenas de texto (str)
    name = "David"
    print(type(name))

    # Booleanos (bool)
    is_student = True
    print(type(is_student))
    is_teacher = False
    print(type(is_teacher))

    # Listas (list)
    numbers = [1, 2, 3, 4, 5]
    print(type(numbers))

    # Diccionarios (dict)
    person = {"name": "David", "age": 25}
    print(type(person))

    # Tuplas (tuple)    
    coordinates = (10, 20)
    print(type(coordinates))

    # Conjuntos (set)
    unique_numbers = {1, 2, 3, 4, 5}
    print(type(unique_numbers))

def ejemplos_conversiones():
    # Conversiones entre tipos
    numero_texto = "42"
    numero = int(numero_texto)  # String a entero
    print(f"String a entero: {numero}")

    numero_decimal = "3.14"
    decimal = float(numero_decimal)  # String a float
    print(f"String a float: {decimal}")

    numero = 42
    texto = str(numero)  # Número a string
    print(f"Número a string: {texto}")

    # Conversiones en casos reales
    edad = "25"
    años_futuros = 10
    edad_futura = int(edad) + años_futuros
    print(f"Dentro de {años_futuros} años tendrás {edad_futura} años")

    # Conversión de lista a tupla y viceversa
    lista_numeros = [1, 2, 3, 4, 5]
    tupla_numeros = tuple(lista_numeros)
    print(f"Lista convertida a tupla: {tupla_numeros}")

    # Conversión de lista a conjunto (elimina duplicados)
    lista_duplicados = [1, 2, 2, 3, 3, 4, 5, 5]
    conjunto_unico = set(lista_duplicados)
    print(f"Lista con duplicados convertida a conjunto: {conjunto_unico}")

if __name__ == "__main__":
    print("\n=== Ejemplos de tipos de datos ===")
    ejemplos_tipos_datos()
    print("\n=== Ejemplos de conversiones ===")
    ejemplos_conversiones() 






# ------------------------ EJEMPLOS MÉTODOS BÁSICOS --------------------------

def ejemplos_print():
    # print básico
    print("Hola Mundo")
    
    # print con múltiples argumentos
    nombre = "Ana"
    edad = 25
    print("Nombre:", nombre, "Edad:", edad)
    
    # print con end (por defecto es \n)
    print("Esta línea", end=" ")
    print("continúa en la misma línea")
    
    # print con sep (separador)
    print("Python", "es", "genial", sep="-")

def ejemplos_type():
    # Verificar tipos de diferentes datos
    datos = [
        42,                    # int
        3.14,                  # float
        "Hola",               # str
        True,                  # bool
        [1, 2, 3],            # list
        (1, 2),               # tuple
        {"a": 1},             # dict
        {1, 2, 3}             # set
    ]
    
    for dato in datos:
        print(f"Valor: {dato} -> Tipo: {type(dato)}")

def ejemplos_input():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola, {nombre}!")

    edad = int(input("Ingrese su edad: "))
    print(f"Usted tiene {edad} años.")

    if edad >= 18:
            print("Usted es mayor de edad.")
    else:
            print("Usted es menor de edad.")


if __name__ == "__main__":
    print("=== Ejemplos de print() ===")
    ejemplos_print()
    
    print("\n=== Ejemplos de type() ===")
    ejemplos_type()
    
    print("\n=== Ejemplos de input() ===")
    ejemplos_input()





# ------------------- OPERADORES ------------------------

"""
Ejemplos de operadores en Python
"""

def operadores_aritmeticos():
    print("\n=== Operadores Aritméticos ===")
    a, b = 10, 3
    
    print(f"Suma: {a} + {b} = {a + b}")
    print(f"Resta: {a} - {b} = {a - b}")
    print(f"Multiplicación: {a} * {b} = {a * b}")
    print(f"División: {a} / {b} = {a / b}")
    print(f"División entera: {a} // {b} = {a // b}")
    print(f"Módulo: {a} % {b} = {a % b}")
    print(f"Potencia: {a} ** {b} = {a ** b}")

def operadores_comparacion():
    print("\n=== Operadores de Comparación ===")
    x, y = 5, 10
    
    print(f"{x} > {y}: {x > y}")
    print(f"{x} < {y}: {x < y}")
    print(f"{x} == {y}: {x == y}")
    print(f"{x} != {y}: {x != y}")
    print(f"{x} >= {y}: {x >= y}")
    print(f"{x} <= {y}: {x <= y}")

def operadores_logicos():
    print("\n=== Operadores Lógicos ===")
    a, b = True, False
    
    print(f"AND: {a} and {b} = {a and b}")
    print(f"OR: {a} or {b} = {a or b}")
    print(f"NOT: not {a} = {not a}")
    
    # Caso real: Validación de edad
    edad = 25
    tiene_licencia = True
    puede_conducir = edad >= 18 and tiene_licencia
    print(f"\nPuede conducir: {puede_conducir}")

def operadores_asignacion():
    print("\n=== Operadores de Asignación ===")
    x = 10
    print(f"x = {x}")
    
    x += 5  # x = x + 5
    print(f"x += 5: {x}")
    
    x -= 3  # x = x - 3
    print(f"x -= 3: {x}")
    
    x *= 2  # x = x * 2
    print(f"x *= 2: {x}")
    
    x /= 4  # x = x / 4
    print(f"x /= 4: {x}")

def operadores_identidad_pertenencia():
    print("\n=== Operadores de Identidad y Pertenencia ===")
    
    # Operadores de identidad (is, is not)
    lista1 = [1, 2, 3]
    lista2 = [1, 2, 3]
    lista3 = lista1
    
    print(f"lista1 is lista2: {lista1 is lista2}")  # False (objetos diferentes)
    print(f"lista1 is lista3: {lista1 is lista3}")  # True (mismo objeto)
    
    # Operadores de pertenencia (in, not in)
    frutas = ["manzana", "plátano", "naranja"]
    print(f"'manzana' in frutas: {'manzana' in frutas}")
    print(f"'uva' not in frutas: {'uva' not in frutas}")

def ejemplo_casos_reales():
    print("\n=== Ejemplos de Casos Reales ===")
    
    # Calculadora de descuento
    precio_original = 100
    descuento = 20
    
    precio_final = precio_original * (1 - descuento/100)
    print(f"Precio original: ${precio_original}")
    print(f"Descuento: {descuento}%")
    print(f"Precio final: ${precio_final}")



# Validación de contraseña
# Definición de la contraseña a validar
contraseña = "Python123"

# Validación de mayúsculas: verifica si existe al menos una letra mayúscula
# any() devuelve True si encuentra al menos un elemento que cumpla la condición
# isupper() verifica si el carácter es una letra mayúscula
tiene_mayuscula = any(c.isupper() for c in contraseña)

# Validación de minúsculas: verifica si existe al menos una letra minúscula
# islower() verifica si el carácter es una letra minúscula
tiene_minuscula = any(c.islower() for c in contraseña)

# Validación de números: verifica si existe al menos un número
# isdigit() verifica si el carácter es un número
tiene_numero = any(c.isdigit() for c in contraseña)

# Validación final: la contraseña es válida si cumple todas las condiciones
# Debe tener al menos una mayúscula, una minúscula y un número
es_valida = tiene_mayuscula and tiene_minuscula and tiene_numero

# Muestra el resultado de la validación
print(f"\nLa contraseña es válida: {es_valida}")

if __name__ == "__main__":
    operadores_aritmeticos()
    operadores_comparacion()
    operadores_logicos()
    operadores_asignacion()
    operadores_identidad_pertenencia()
    ejemplo_casos_reales() 