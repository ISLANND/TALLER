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



