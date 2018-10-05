from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread('pedestrian_00013.png')

# We have three channels (RGB) for each pixel and 
# we cannot apply histogram equalization on the three channels 
# in a separate manner.

# Separar os canais
canais = cv2.split(img)
cores = ('blue', 'green', 'red')

plt.figure()
plt.title("'Histograma Colorido")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")

for (canal, cor) in zip(canais, cores):
    #Este loop executa 3 vezes, uma para cada canal
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, color = cor)
    plt.xlim([0, 256])

plt.show()
