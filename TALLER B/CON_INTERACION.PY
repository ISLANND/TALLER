# 1. Cálculo de la potencia eléctrica

# Ingreso de datos
voltaje = float(input("Ingrese el valor del voltaje (V): "))
corriente = float(input("Ingrese el valor de la corriente (A): "))

# Cálculo de la potencia
potencia = voltaje * corriente

# Resultado
print(f"La potencia consumida por el circuito es: {potencia} W")

# 2. Realice un programa que calcule X números aleatorios en un rango determinado por el usuario. 

import random

c = int(input("Ingrese cuántos datos desea: "))
a = int(input("Ingrese el límite inferior: "))
b = int(input("Ingrese el límite superior: "))

numeros = [random.randint(a, b) for _ in range(c)]

print("Sus números dentro del rango deseado son:", numeros)


# 3. Realice un programa para el cálculo de volúmenes (Prisma, Pirámide, Cono truncado, Cilindro) 
# donde el usuario pueda seleccionar el sólido y los parámetros de cada volumen. 

import math

print("Para calcular el volumen escoge:")
print("1. Prisma Rectangular")
print("2. Pirámide")
print("3. Cono truncado")
print("4. Cilindro")

i = int(input("Ingresa el sólido a calcular: "))

if i == 1:
    print("Escogiste 1. Volumen de un Prisma Rectangular")
    a = float(input("Valor del largo en cm: "))
    b = float(input("Valor del ancho en cm: "))
    c = float(input("Valor de la altura en cm: "))
    v = a * b * c
    print("El volumen del prisma es:", v, "cm³")

elif i == 2:
    print("Escogiste 2. Volumen de una Pirámide")
    a = float(input("Valor de la base en cm: "))
    b = float(input("Valor de la altura en cm: "))
    v = (1/3) * a**2 * b
    print("El volumen de la pirámide es:", v, "cm³")

elif i == 3:
    print("Escogiste 3. Volumen de un cono truncado")
    a = float(input("Valor de la altura en cm: "))
    b = float(input("Ingresa el radio 1 en cm: "))
    c = float(input("Ingresa el radio 2 en cm: "))
    v = (a * math.pi / 3) * (b**2 + c**2 + b * c)
    print("El volumen del cono truncado es:", v, "cm³")

elif i == 4:
    print("Escogiste 4. Volumen de un cilindro")
    a = float(input("Valor de la altura en cm: "))
    b = float(input("Ingresa el radio en cm: "))
    v = math.pi * b**2 * a
    print("El volumen del cilindro es:", v, "cm³")

else:
    print("Opción equivocada, vuelve a intentarlo")


#4. Realice un programa que le permita al usuario escoger entre robot Cilíndrico, Cartesiano y esférico, 
#   donde como respuesta a la selección conteste con el tipo y número de articulaciones que posee. 

print("Escoge:")
print("1. Robot Cilíndrico")
print("2. Robot Cartesiano")
print("3. Robot Esférico")

i = int(input("¿Cuál escoges?: "))

if i == 1:
    print("Escogiste el robot cilíndrico: 1 articulación rotacional y 2 prismáticas (3 en total)")
elif i == 2:
    print("Escogiste el robot cartesiano: 3 articulaciones prismáticas")
elif i == 3:
    print("Escogiste el robot esférico: 2 articulaciones prismáticas y 1 rotacional (3 en total)")


# 5.Escribir un programa que realice la pregunta ¿Desea continuar Si/No? y que no deje de hacerla 
#  hasta que el usuario teclee No. 



while True:
    txt = input("¿Desea continuar Si/No?: ").lower()
    if txt == "no":
        break
