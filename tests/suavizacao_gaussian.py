import cv2
import numpy as np
from matplotlib import pyplot as plt

# Este método é mais lento para calcular que os anteriores mas como vantagem
# apresenta a preservação de bordas e garante que o ruído seja removido

img = cv2.imread('pedestrian_test_clahe_2.jpg', 0)

# Tests

suave = cv2.GaussianBlur(img, (11, 11), 0)

cv2.imshow("11", suave)
cv2.waitKey(0)
cv2.imwrite("pedestrian_test_gaussian.png", suave)

cv2.imshow("7", cv2.GaussianBlur(img, (7, 7), 0))
cv2.waitKey(0)

#img = img[::2,::2] # Diminui a imagem

#suave = np.vstack([
# np.hstack([img,
# cv2.GaussianBlur(img, ( 3, 3), 0)]),
# np.hstack([cv2.GaussianBlur(img, ( 5, 5), 0),
# cv2.GaussianBlur(img, ( 7, 7), 0)]),
# np.hstack([cv2.GaussianBlur(img, ( 9, 9), 0),
# cv2.GaussianBlur(img, (11, 11), 0)]),
# ])

#cv2.imshow("Suavizada", suave)
#cv2.waitKey(0)
