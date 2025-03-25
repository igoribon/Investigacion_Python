# Definimos las operaciones que vamos a usar en la calculadora
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División entre cero no permitida"
    
def factorial(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1
    return r


# Definimos una función para pedir los números al usuario
def inputs():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    return num1, num2


# Mostramos el menú de la calculadora
print("Bienvenido a la calculadora en Python")
print("Opciones:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Elevar a una potencia")
print("6. realizar una raiz")
print("7. Calcular el factorial de un número")


# Pedimos al usuario que elija una opción
opcion = int(input("Elige una opción (1/2/3/4/5/6/7): "))


# Realizamos la operación correspondiente
if opcion == 1:
    num1, num2 = inputs()
    print("Resultado:", suma(num1, num2))
elif opcion == 2:
    num1, num2 = inputs()
    print("Resultado:", resta(num1, num2))
elif opcion == 3:
    num1, num2 = inputs()
    print("Resultado:", multiplicacion(num1, num2))
elif opcion == 4:
    num1, num2 = inputs()
    print("Resultado:", division(num1, num2))
elif opcion == 5:
    num1, num2 = inputs()
    print("Resultado:", num1**num2)
elif opcion == 6:
    num1, num2 = inputs()
    print("Resultado:", num1**(1/num2))
elif opcion == 7:
    num1 = float(input("Ingresa el número a factorizar: "))
    print("Resultado:", factorial(num1))
else:
    print("Opción no válida")