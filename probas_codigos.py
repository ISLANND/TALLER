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