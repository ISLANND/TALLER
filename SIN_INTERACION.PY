# Taller 1 Robótica
# A. Sin interacción de consola


import math
import numpy as np



# --------------------------------------------------
# 1. Operaciones básicas 
# --------------------------------------------------

# Vectores inicializados
v1 = np.array([2, 4, 6])
v2 = np.array([1, 3, 5])

suma = v1 + v2
resta = v1 - v2
producto_punto = np.dot(v1, v2)
producto_cruz = np.cross(v1, v2)
division = v1 / v2

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Suma:", suma)
print("Resta:", resta)
print("Producto punto:", producto_punto)
print("Producto cruz:", producto_cruz)
print("División:", division)
# #------------------------------------------------------------------------------
# #2 division de matrices
# #---------------------------------------------------------------------------

import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

suma = A + B
resta = A - B
multiplicacion = np.dot(A, B)     # Producto matricial
producto_punto = np.sum(A * B)    # Producto punto
division_elemento = A / B         # División elemento a elemento

# División como multiplicación por la inversa
division_inversa = np.dot(A, np.linalg.inv(B))

print("Suma:\n", suma)
print("Resta:\n", resta)
print("Multiplicación:\n", multiplicacion)
print("Producto punto:", producto_punto)
print("División elemento a elemento:\n", division_elemento)
print("División usando inversa:\n", division_inversa)

#-------------------------------------------------

# --------------------------------------------------
# 3. Conversión de coordenadas
# Rectangulares → Cilíndricas → Esféricas
# --------------------------------------------------

x = 4
y = 3
z = 1

# Rectangulares a cilíndricas
r = math.sqrt(x**2 + y**2)
theta = math.degrees(math.atan(y / x))
z1 = z

print("\nCilíndricas:")
print("r =", r)
print("theta =", theta)
print("z =", z1)

# Cilíndricas a rectangulares
x1 = r * math.cos(math.radians(theta))
y1 = r * math.sin(math.radians(theta))

print("\nRectangulares desde cilíndricas:")
print("x =", x1)
print("y =", y1)
print("z =", z1)

# Rectangulares a esféricas
rho = math.sqrt(x**2 + y**2 + z**2)
phi = math.degrees(math.acos(z / rho))

print("\nEsféricas:")
print("rho =", rho)
print("phi =", phi)
print("theta =", theta)

# Esféricas a rectangulares
x2 = rho * math.sin(math.radians(phi)) * math.cos(math.radians(theta))
y2 = rho * math.sin(math.radians(phi)) * math.sin(math.radians(theta))
z3 = rho * math.cos(math.radians(phi))

print("\nRectangulares desde esféricas:")
print("x =", x2)
print("y =", y2)
print("z =", z3)

# --------------------------------------------------
# 4. RTD PT100 – Resistencia en función de temperatura
# --------------------------------------------------

a = 3.9083e-3
b = -5.775e-7
c = -4.183e-12
r0 = 100

def resistencia_pt100(t):
    if t >= 0:
        return r0 * (1 + a*t + b*t**2)
    else:
        return r0 * (1 + a*t + b*t**2 + c*(t - 100)*t**3)

t = 200
rt = resistencia_pt100(t)
print("\nRTD a 200°C:", rt, "Ω")

t = 0
rt = resistencia_pt100(t)
print("RTD a 0°C:", rt, "Ω")

# --------------------------------------------------
# 5. Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo) 
#     y un parámetro de salida (matriz). 
# --------------------------------------------------
import numpy as np

def rotacion_x(angulo):
    theta = np.radians(angulo)  # Convertir a radianes
    matriz = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])
    return matriz


def rotacion_y(angulo):
    theta = np.radians(angulo)
    matriz = np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return matriz


def rotacion_z(angulo):
    theta = np.radians(angulo)
    matriz = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])
    return matriz
print("Rotación en X (0°):")
print(rotacion_x(0))

print("\nRotación en Y (0°):")
print(rotacion_y(0))

print("\nRotación en Z (0°):")
print(rotacion_z(0))
# --------------------------------------------------
# 6. Fuerza de cilindro neumático doble efecto
# --------------------------------------------------

# Datos del cilindro
D = 100**2   # mm²
d = 20**2    # mm²
Bar = 6      # presión en bar

Av = (math.pi * D) / 4       # Área de avance
Ar = (math.pi * (D - d)) / 4 # Área de retroceso

Fv = Av * (Bar / 10)         # Fuerza de avance
Fr = Ar * (Bar / 10)         # Fuerza de retroceso

print("\nCilindro neumático:")
print("Fuerza de avance:", Fv)
print("Fuerza de retroceso:", Fr)
