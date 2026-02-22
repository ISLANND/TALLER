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