import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Cargar imagen
imagen = cv2.imread("logo.png")

# 2. Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# 3. Umbralizar (hacer blanco y negro)
_, binaria = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)

# 4. Encontrar contornos
contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 5. Tomar el contorno más grande (el logo)
contorno_principal = max(contornos, key=cv2.contourArea)

# 6. Extraer coordenadas
coordenadas = contorno_principal.squeeze()

# Mostrar primeras 10 coordenadas
print(coordenadas[:10])