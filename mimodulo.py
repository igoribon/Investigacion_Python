# mimodulo.py

def saludar(nombre):
    return f"Hola, {nombre}!"

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        return f"{self.nombre} tiene {self.edad} años."

variable_modulo = "Soy una variable del módulo."

__all__ = ["saludar", "Persona", "variable_modulo"]  # Especial de módulo para controlar qué se importa

# Estructura de un paquete
# /mipaquete
#   __init__.py
#   modulo1.py
#   modulo2.py

# contenido de modulo1.py# mimodulo.py

def saludar(nombre):
    return f"Hola, {nombre}!"

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        return f"{self.nombre} tiene {self.edad} años."

variable_modulo = "Soy una variable del módulo."

__all__ = ["saludar", "Persona", "variable_modulo"]  # Especial de módulo para controlar qué se importa

# Estructura de un paquete
# /mipaquete
#   __init__.py
#   modulo1.py
#   modulo2.py

# contenido de modulo1.py
def funcion_modulo1():
    return "Función del módulo 1"

# contenido de modulo2.py
def funcion_modulo2():
    return "Función del módulo 2"

# importar desde un paquete
import sys
import os

# Add the directory containing 'mipaquete' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../mipaquete')))

from mipaquete import modulo1, modulo2
print(modulo1.funcion_modulo1())
print(modulo2.funcion_modulo2())

# Librerías
import math
import random as rd
import os
import sys

# Ejemplo de math
print(math.sqrt(16))  # Raíz cuadrada de 16

# Ejemplo de random
print(rd.randint(1, 10))  # Número aleatorio entre 1 y 10

# Ejemplo de os
print(os.getcwd())  # Directorio de trabajo actual

# Ejemplo de sys
print(sys.version)  # Versión de Python

def funcion_modulo1():
    return "Función del módulo 1"

# contenido de modulo2.py
def funcion_modulo2():
    return "Función del módulo 2"

# importar desde un paquete
from mipaquete import modulo1, modulo2
print(modulo1.funcion_modulo1())
print(modulo2.funcion_modulo2())

# Librerías
import math
import random as rd
import os
import sys

# Ejemplo de math
print(math.sqrt(16))  # Raíz cuadrada de 16

# Ejemplo de random
print(rd.randint(1, 10))  # Número aleatorio entre 1 y 10

# Ejemplo de os
print(os.getcwd())  # Directorio de trabajo actual

# Ejemplo de sys
print(sys.version)  # Versión de Python