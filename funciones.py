def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("David")) # Hola, David!

# Argumentos en Funciones

#Argumentos Posicionales

def suma(a, b):
    return a + b

print(suma(5, 3)) # 8

# Argumentos por Nombre

def saludar2(nombre, apellido, edad):
    return f"Hola, {nombre} {apellido}! Tienes {edad} años."

print(saludar2(nombre="David", apellido="Bustos", edad=25)) # Hola, David García! Tienes 25 años.

# Argumentos con valores por defecto    

def saludar3(nombre, apellido, edad=25):
    return f"Hola, {nombre} {apellido}! Tienes {edad} años."

print(saludar3(nombre="David", apellido="Bustos")) # Hola, David García! Tienes 25 años.



# Funciones Avanzadas

# Funciones Lambda

suma = lambda a, b: a + b

print(suma(5, 3)) # 8

# Ejemplo de uso de lambda con condicional

pares = lambda x: "Par" if x % 2 == 0 else "Impar"

print(pares(2)) # Par
print(pares(3)) # Impar

mayoria_edad = lambda edad: "Eres mayor de Edad" if edad >= 18 else "Eres menor de Edad"

print(mayoria_edad(25)) # Eres mayor de Edad
print(mayoria_edad(15)) # Eres menor de Edad

# Lambda con map

numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda x: x**2, numeros))

print(cuadrados) # [1, 4, 9, 16, 25]

# Lambda con filter
# Ejemplo con numeros pares
numb = [1, 2, 3, 4, 5]

pares = list(filter(lambda x: x % 2 == 0, numb))

print(pares) # [2, 4]

# Ejemlpo: Filtrar palabras largas

palabras = ["python", "java", "javascript", "c++"]

largas = list(filter(lambda x: len(x) > 5, palabras))

print(largas) # ["python", "javascript"]

# Funcion Reduce

from functools import reduce

numeros = [1, 2, 3, 4, 5]

suma = reduce(lambda x, y: x + y, numeros)

print(suma) # 15

# 2 ejemplo encontrar el numero mayor de una lista
from functools import reduce

numeros = [7, 2, 9, 3, 6]
mayor = reduce(lambda x, y: x if x > y else y, numeros)

print(mayor)  # 9

# Funcion Zip

nombres = ["David", "Juan", "Maria"]
edades = [25, 30, 28]

personas = list(zip(nombres, edades))

print(personas) # [('David', 25), ('Juan', 30), ('Maria', 28)]

# Iterando sobre una lista de tuplas
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

    
# Ejemplo adicional de zip con calificaciones
materias = ["Matemáticas", "Historia", "Ciencias"]
calificaciones = [85, 92, 78] 
creditos = [4, 3, 5]

# Combinar las tres listas
registro_academico = list(zip(materias, calificaciones, creditos))

print("\nRegistro Académico:")
for materia, nota, credito in registro_academico:
    print(f"Materia: {materia}, Nota: {nota}, Créditos: {credito}")

# Calcular promedio ponderado
total_puntos = sum(nota * credito for nota, credito in zip(calificaciones, creditos))
total_creditos = sum(creditos)
promedio = total_puntos / total_creditos

print(f"\nPromedio ponderado: {promedio:.2f}")


def descripcion_persona(*args, **kwargs):
    print("Detalles de la persona:")
    for arg in args:
        print(f"- {arg}")

    print("\nInformación adicional:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

descripcion_persona("Estudiante", "Programador", nombre="David", edad=30, ciudad="Madrid")


# Detalles de la persona:
# - Estudiante
# - Programador

# Información adicional:
# nombre: David
# edad: 30
# ciudad: Madrid

# Ejemplo 5: Crear una función flexible

def crear_perfil(nombre, *habilidades, **detalles):
    print(f"Perfil de {nombre}:")
    print("Habilidades:", ", ".join(habilidades))
    
    print("\nDetalles adicionales:")
    for clave, valor in detalles.items():
        print(f"{clave}: {valor}")

crear_perfil("Ana", "Python", "Django", "SQL", edad=25, ciudad="Barcelona", experiencia="3 años")

# Perfil de Ana:
# Habilidades: Python, Django, SQL

# Detalles adicionales:
# edad: 25
# ciudad: Barcelona

# Función con *args (argumentos posicionales variables)
def sumar_numeros(*args):
    """
    Esta función acepta cualquier cantidad de números y los suma.
    *args permite pasar un número variable de argumentos posicionales.
    """
    total = 0
    for numero in args:
        total += numero
    return total

# Función con **kwargs (argumentos con nombre variables) 
def info_usuario(**kwargs):
    """
    Esta función acepta cualquier cantidad de pares clave-valor.
    **kwargs permite pasar un número variable de argumentos con nombre.
    """
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Función que combina *args y **kwargs
def funcion_combinada(*args, **kwargs):
    """
    Esta función combina tanto argumentos posicionales como argumentos con nombre.
    Primero procesa los args y luego los kwargs.
    """
    print("Argumentos posicionales (*args):")
    for arg in args:
        print(f"- {arg}")
        
    print("\nArgumentos con nombre (**kwargs):")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Ejemplos de uso
print("\nEjemplo de *args:")
resultado = sumar_numeros(1, 2, 3, 4, 5)
print(f"La suma es: {resultado}")

print("\nEjemplo de **kwargs:")
info_usuario(nombre="Ana", edad=25, ciudad="Madrid")

print("\nEjemplo combinado:")
funcion_combinada("Python", "JavaScript", "SQL", 
    nombre="David", edad=30, experiencia="5 años")
