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



