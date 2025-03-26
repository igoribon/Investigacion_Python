
cadena = "Un fantasma recorre Europa"

# capitalize(): Convierte el primer carácter en mayúscula y el resto en minúscula.
print("capitalize():", cadena.capitalize())

# title(): Convierte la primera letra de cada palabra en mayúscula.
print("title():", cadena.title())

# upper(): Convierte todos los caracteres de la cadena en mayúsculas.
print("upper():", cadena.upper())

# lower(): Convierte todos los caracteres de la cadena en minúsculas.
print("lower():", cadena.lower())

# swapcase(): Intercambia mayúsculas por minúsculas y viceversa.
print("swapcase():", cadena.swapcase())

# find(): Busca la primera aparición de una subcadena y devuelve su posición.
print("find('mundo'):", cadena.find("mundo"))  # Devuelve la posición inicial de 'mundo'.

# rfind(): Busca la última aparición de una subcadena y devuelve su posición.
print("rfind('o'):", cadena.rfind("o"))  # Devuelve la última posición de 'o'.

# replace(): Reemplaza todas las coincidencias de una subcadena con otra.
print("replace('mundo', 'Python'):", cadena.replace("mundo", "Python"))

# strip(): Elimina espacios o caracteres especificados del inicio y final de la cadena.
cadena_espacios = "   hola   "
print("strip():", cadena_espacios.strip())  # Elimina espacios al inicio y final.

# lstrip(): Elimina espacios o caracteres especificados del inicio de la cadena.
print("lstrip():", cadena_espacios.lstrip())  # Elimina espacios al inicio.

# rstrip(): Elimina espacios o caracteres especificados del final de la cadena.
print("rstrip():", cadena_espacios.rstrip())  # Elimina espacios al final.

# split(): Divide la cadena en una lista usando un separador.
cadena_split = "uno,dos,tres"
print("split():", cadena_split.split(","))  # Divide la cadena por comas.

# rsplit(): Similar a split(), pero divide desde la derecha.
print("rsplit(',', 1):", cadena_split.rsplit(",", 1))  # Divide solo una vez desde la derecha.

# join(): Une los elementos de un iterable en una sola cadena, usando un separador.
lista_palabras = ["hola", "mundo"]
print("join():", "-".join(lista_palabras))  # Une las palabras con '-'.

# startswith(): Verifica si la cadena comienza con una subcadena específica.
print("startswith('hola'):", cadena.startswith("hola"))  # True si empieza con 'hola'.

# endswith(): Verifica si la cadena termina con una subcadena específica.
print("endswith('mundo'):", cadena.endswith("mundo"))  # True si termina con 'mundo'.

# isalpha(): Verifica si todos los caracteres de la cadena son alfabéticos.
print("isalpha():", cadena.isalpha())  # False porque hay un espacio.

# isspace(): Verifica si todos los caracteres de la cadena son espacios en blanco.
print("isspace():", "   ".isspace())  # True porque todos son espacios.

# center(): Centra la cadena en un espacio de longitud dada, rellenando con caracteres opcionales.
print("center(20, '*'):", cadena.center(20, "*"))  # Centra la cadena con '*'.

# ljust(): Alinea la cadena a la izquierda en un espacio de longitud dada.
print("ljust(20, '*'):", cadena.ljust(20, "*"))  # Alinea a la izquierda.

# rjust(): Alinea la cadena a la derecha en un espacio de longitud dada.
print("rjust(20, '*'):", cadena.rjust(20, "*"))  # Alinea a la derecha.


# ==========================
# Métodos de diccionarios (dict)
# ==========================
diccionario = {"a": 1, "b": 2}

# fromkeys(): Crea un nuevo diccionario con claves de un iterable y valores opcionales.
nuevo_diccionario = dict.fromkeys(["x", "y"], 0)  # Claves: 'x', 'y'; Valor predeterminado: 0.
print("fromkeys():", nuevo_diccionario)

# get(): Obtiene el valor asociado a una clave, o un valor predeterminado si no existe.
print("get('a'):", diccionario.get("a"))  # Obtiene el valor de 'a'.
print("get('c', 0):", diccionario.get("c", 0))  # Devuelve 0 si 'c' no existe.

# update(): Actualiza el diccionario con pares clave-valor de otro iterable.
diccionario.update({"c": 3})  # Agrega o actualiza la clave 'c'.
print("update():", diccionario)

# values(): Devuelve una vista de los valores del diccionario.
print("values():", list(diccionario.values()))  # Lista de valores: [1, 2, 3].


# ==========================
# Métodos de listas (list)
# ==========================
lista = [1, 2, 3]

# append(): Agrega un elemento al final de la lista.
lista.append(4)  # Agrega el número 4.
print("append():", lista)

# extend(): Agrega múltiples elementos de un iterable al final de la lista.
lista.extend([5, 6])  # Agrega [5, 6].
print("extend():", lista)

# insert(): Inserta un elemento en una posición específica de la lista.
lista.insert(0, 0)  # Inserta el número 0 en la posición 0.
print("insert():", lista)

# remove(): Elimina la primera aparición de un elemento específico.
lista.remove(3)  # Elimina el número 3.
print("remove():", lista)

# pop(): Elimina y devuelve el elemento en una posición específica.
elemento_eliminado = lista.pop(2)  # Elimina el elemento en la posición 2.
print("pop():", lista, "Eliminado:", elemento_eliminado)

# clear(): Elimina todos los elementos de la lista.
lista.clear()  # Vacía la lista.
print("clear():", lista)

# index(): Encuentra la primera aparición de un elemento en la lista.
lista = [1, 2, 3, 2]
print("index(2):", lista.index(2))  # Posición de la primera aparición de 2.

# count(): Cuenta cuántas veces aparece un elemento en la lista.
print("count(2):", lista.count(2))  # Número de veces que aparece el 2.

# reverse(): Invierte el orden de los elementos de la lista.
lista.reverse()  # Invierte el orden.
print("reverse():", lista)

# copy(): Crea una copia superficial de la lista.
lista_copia = lista.copy()  # Copia la lista.
print("copy():", lista_copia)

# sort(): Ordena los elementos de la lista (ascendente o descendente).
lista.sort(reverse=True)  # Ordena en orden descendente.
print("sort():", lista)


# ==========================
# Condicionales
# ==========================
numero = 10

# if, elif, else: Evalúa condiciones secuenciales y ejecuta el bloque correspondiente.
if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es cero")
else:
    print("El número es negativo")

# Ternaria: Forma compacta de escribir una condicional simple.
mensaje = "Positivo" if numero > 0 else "No positivo"
print("Ternaria:", mensaje)