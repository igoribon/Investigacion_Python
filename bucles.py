# bucle for
print ("\n""Bucle for")
for i in "Python":
    print(i)


# bucle con iteración
print ("\n""Bucle con iteración")
lista = [2, 3, 5, 6]
it = iter(lista)
print(next(it))
print(next(it))

# Bucle for con range
print ("\n""Bucle for con range")
for i in range(5, 20, 2):
    print(i) 


# While con else
print ("\n""While con else")
contador = 0
while contador < 3:
    print(f"El contador es {contador}")
    contador += 1
else:
    print("El bucle ha terminado porque la condición ya no se cumple.\n")


# Bucle usando las instrucciones continue y break
print ("Bucle usando las instrucciones continue y break")
for numero in range(1, 6):  # Iteramos del 1 al 5
    if numero == 3:
        print("Se usa continue para saltar el número 3.")
        continue
    if numero == 5:
        print("Se usa break para detener el bucle en el número 5.\n")
        break
    print(f"Número: {numero}")

# Bucle que usa list comprenhension
numeros_pares = [x for x in range(10) if x % 2 == 0]
print ("LIST COMPRENHENSION")
print(numeros_pares)

# bucle con elif
print ("\n""Bucle con elif")
numero = int(input("Introduce un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero == 0:
    print("El número es cero.")
else:
    print("El número es negativo.""\n")

#Bucle con Match y case
dia = input("Introduce un día de la semana: ").lower()
match dia:
    case "lunes":
        print("Es el primer día laboral de la semana.""\n")
    case "sabado" | "domingo":
        print("¡Es fin de semana!""\n")
    case _:
        print("Es un día laboral.""\n")

# Bucle con Zip
# Listas para combinar
print ("Bucle con Zip")
colores = ["rojo", "verde", "azul"]
frutas = ["manzana", "pera", "mora", "plátano"]

# Iteramos con zip
for color, fruta in zip(colores, frutas):
    print(f"La {fruta} es de color {color}.")
