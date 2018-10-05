import numpy as np
import cv2

img = cv2.imread('pedestrian_00013.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

(canalAzul, canalVerde, canalVermelho) = cv2.split(hsv)

zeros = np.zeros(img.shape[:2], dtype = "uint8")

cv2.imshow("Vermelho", cv2.merge([zeros, zeros, canalVermelho]))
cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros]))
cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros]))
cv2.imshow("Original", img)
cv2.waitKey(0)
