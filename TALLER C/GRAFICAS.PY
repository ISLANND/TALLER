#1. Realice un programa que grafique el comportamiento de un sensor PT100 desde -200°C a 200°C. 
import numpy as np
import matplotlib.pyplot as plt

# Rango de temperatura
x = np.linspace(-200, 200, 400)

# Función lineal del PT100
y = 0.373505 * x + 100


# Gráfica
plt.plot(x, y, linewidth=1.5)

# Límites de los ejes
plt.axis([-200, 200, 0, 200])

# Rótulos y título
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (Ω)")
plt.title("PT100")

# Mostrar gráfica
plt.grid(True)
plt.show()

#----------------------------------------------------------------------------

#3. Implemente la ecuación de carga y descarga para un circuito RC. El usuario ingresa por teclado el 
# valor de voltaje (V), capacitancia (𝜇𝐹) y resistencia (Ω).  Posteriormente realice en Python la 
# gráfica.
import numpy as np
import matplotlib.pyplot as plt


# Entrada de datos
E = float(input("Ingresa el valor del voltaje (V): "))
R = float(input("Ingresa el valor de la resistencia (Ω): "))
C_uF = float(input("Ingresa el valor del capacitor (uF): "))

# Conversión de microfaradios a faradios
C = C_uF * 1e-6

# Constante de tiempo
tau = R * C
print("Constante de tiempo tau =", tau, "s")

# Vector de tiempo (0 a 5 tau)
t = np.arange(0, 5 * tau, 0.01)

# Ecuaciones
Vc = E * (1 - np.exp(-t / tau))      # Voltaje de carga
Vd = E * np.exp(-t / tau)            # Voltaje de descarga

# Gráfica
plt.plot(t, Vc, label="Carga del capacitor")
plt.plot(t, Vd, label="Descarga del capacitor")

plt.title("Fase de carga y descarga del capacitor (RC)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.legend()
plt.grid(True)
plt.show()

#----------------------------------------------------------------------------
# 2. Realice un programa que le permita al usuario ingresar los coeficientes de una función de 
# transferencia de segundo orden y graficar su comportamiento, además se debe mostrar que tipo 
# de sistema es: subamortiguado, criticamente amortiguado y sobreamortiguado. 
# --- Análisis de sistema de segundo orden ---
import numpy as np
import matplotlib.pyplot as plt

# Ingreso de coeficientes
print("Ingrese los coeficientes de la función de transferencia de segundo orden:")
num = float(input("Coeficiente del numerador (ganancia): "))
den2 = float(input("Coeficiente de s^2: "))
den1 = float(input("Coeficiente de s: "))
den0 = float(input("Coeficiente independiente: "))

wn = np.sqrt(den0/den2)
zeta = den1/(2*np.sqrt(den2*den0))

# Determinar tipo de sistema
if zeta < 1:
	tipo = "Subamortiguado"
elif np.isclose(zeta, 1):
	tipo = "Críticamente amortiguado"
else:
	tipo = "Sobreamortiguado"

print(f"\nTipo de sistema: {tipo}")
print(f"Frecuencia natural (wn): {wn:.3f}")
print(f"Coeficiente de amortiguamiento (zeta): {zeta:.3f}")

# Respuesta al escalón unitario
from scipy.signal import lti, step
sys = lti([num], [den2, den1, den0])
t, y = step(sys)

# Gráfica
plt.plot(t, y)
plt.title(f"Respuesta al escalón - {tipo}")
plt.xlabel("Tiempo (s)")
plt.ylabel("Salida")
plt.grid(True)
plt.show()

#---------------------------------------------------------------

# 4.Elabore un sistema coordenado x, y, z donde se dibuje un vector con coordenadas
# ingresdadas por el usuario, y se grafique en un espacio tridimensional.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Necesario para gráficos 3D

numx = float(input("CORDENADA EN X: "))
numy = float(input("CORDENADA EN Y: "))
numz = float(input("CORDENADA EN Z: "))

vector = np.array([numx, numy, numz], dtype=float)

print("Vector:", vector)

# Magnitud
magnitud = np.linalg.norm(vector)
print("Magnitud del vector:", magnitud)

# Evitar división entre cero
if magnitud != 0:
    print("Vector normalizado:", vector / magnitud)
else:
    print("No se puede normalizar el vector cero")

# Crear figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar el vector
ax.quiver(0, 0, 0, numx, numy, numz, color='red', arrow_length_ratio=0.1)

# Ajustar límites
max_range = max(abs(numx), abs(numy), abs(numz), 1)
ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])

# Etiquetas
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f"Vector 3D: ({numx}, {numy}, {numz})")

plt.show()


#---------------------------------------------------------------
# 5 . Plotee los nombres de los integrantes del grupo en 2D teniendo en cuenta 
# lienas rectas y curvas.

import numpy as np
import matplotlib.pyplot as plt

# =========================
# FUNCIONES AUXILIARES
# =========================
def linea(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], 'k')

def circulo(xc, yc, r, t1=0, t2=2*np.pi):
    t = np.linspace(t1, t2, 100)
    x = xc + r*np.cos(t)
    y = yc + r*np.sin(t)
    plt.plot(x, y, 'k')

# =========================
# DEFINICIÓN DE LETRAS
# =========================
def N(x,y):
    linea(x,y, x,y+2)
    linea(x+1,y, x+1,y+2)
    linea(x,y+2, x+1,y)

def E(x,y):
    linea(x,y, x,y+2)
    linea(x,y+2, x+1,y+2)
    linea(x,y+1, x+0.8,y+1)
    linea(x,y, x+1,y)

def S(x,y):
    # Parte superior de la S
    t = np.linspace(np.pi/2, 3*np.pi/2, 100)
    plt.plot(x+0.5+0.5*np.cos(t), y+1.5+0.5*np.sin(t), 'k')

    # Parte inferior de la S
    t = np.linspace(-np.pi/2, np.pi/2, 100)
    plt.plot(x+0.5+0.5*np.cos(t), y+0.5+0.5*np.sin(t), 'k')
    
def T(x,y):
    linea(x,y+2, x+1,y+2)
    linea(x+0.5,y+2, x+0.5,y)

def O(x,y):
    circulo(x+0.5,y+1,0.5)

def R(x,y):
    linea(x,y, x,y+2)
    circulo(x+0.4,y+1.5,0.5,-np.pi/2,np.pi/2)
    linea(x,y+1, x+1,y)

def L(x,y):
    linea(x,y, x,y+2)
    linea(x,y, x+1,y)

def U(x,y):
    linea(x,y+2, x,y+0.5)
    linea(x+1,y+2, x+1,y+0.5)
    circulo(x+0.5,y+0.5,0.5,np.pi,2*np.pi)

def I(x,y):
    linea(x+0.5,y, x+0.5,y+2)

def A(x,y):
    linea(x,y, x+0.5,y+2)
    linea(x+1,y, x+0.5,y+2)
    linea(x+0.25,y+1, x+0.75,y+1)

def G(x, y):
    # Curva principal (casi un círculo, deja apertura)
    t = np.linspace(0.3*np.pi, 1.7*np.pi, 150)
    xg = x + 0.5 + 0.5*np.cos(t)
    yg = y + 1 + 0.5*np.sin(t)
    plt.plot(xg, yg, 'k')

    # Segmento horizontal interno (gancho de la G)
    plt.plot([x + 0.5, x + 0.9], [y + 1, y + 1], 'k')

    # Segmento vertical corto (cierre parcial)
    plt.plot([x + 0.9, x + 0.9], [y + 1, y + 0.7], 'k')
# =========================
# DIBUJO DE LOS NOMBRES
# =========================
plt.figure(figsize=(12,6))

# ---- NESTOR ----
N(0,0); E(2,0); S(4,0); T(6,0); O(8,0); R(10,0)

# ---- LUISA ----
L(0,-4); U(2,-4); I(4,-4); S(6,-4); A(8,-4)

# ---- SERGIO ----
S(0,-8); E(2,-8); R(4,-8); G(6,-8); I(8,-8); O(10,-8)

# =========================
# AJUSTES DEL PLOT
# =========================
plt.title("Nombres del grupo dibujados en 2D usando líneas y curvas")
plt.axis("equal")
plt.axis("off")
plt.show()

#---------------------------------------------------------------

#6. Obtenga las coordenadas X y Y de los contornos de dos logos de automóviles (Chevrolet, Hyundai, 
# Mazda, etc.), a través de Python. 

import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread("lambo.png")


if imagen is None:
    raise FileNotFoundError("No se pudo cargar la imagen")

gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gris, (5,5), 0)

_, binaria = cv2.threshold(
    blur, 0, 255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

contornos, jerarquia = cv2.findContours(
    binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE
)

print(f"Se detectaron {len(contornos)} contornos")

plt.figure(figsize=(6,6))
for c in contornos:
    if cv2.contourArea(c) > 200:
        coords = c.squeeze()
        if coords.ndim == 2:
            plt.plot(coords[:,0], coords[:,1])

plt.gca().invert_yaxis()
plt.gca().set_aspect('equal')
plt.show()



