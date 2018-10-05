import cv2
import numpy as np
from matplotlib import pyplot as plt

# Este método é mais lento para calcular que os anteriores mas como vantagem
# apresenta a preservação de bordas e garante que o ruído seja removido

img = cv2.imread('pedestrian_test_clahe_2.jpg', 0)

# Tests

suave = cv2.medianBlur(img, 11)

cv2.imshow("11", suave)
cv2.waitKey(0)
cv2.imwrite("pedestrian_test_median.png", suave)

cv2.imshow("7", cv2.medianBlur(img, 7))
cv2.waitKey(0)

#suave = np.vstack([
# np.hstack([img,
# cv2.medianBlur(img, 3)]),
# np.hstack([cv2.medianBlur(img, 5),
# cv2.medianBlur(img, 7)]),
# np.hstack([cv2.medianBlur(img, 9),
# cv2.medianBlur(img, 11)]),
# ])

#cv2.imshow("Suavizada", suave)
#cv2.waitKey(0)
