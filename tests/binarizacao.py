import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pedestrian_test_clahe_2.jpg', 0)

#Thresholding pode ser traduzido por limiarização e no caso de processamento de
#imagens na maior parte das vezes utilizamos para binarização da imagem. Normalmente
#convertemos imagens em tons de cinza para imagens preto e branco onde todos os pixels
#possuem 0 ou 255 como valores de intensidade.

suave = cv2.GaussianBlur(img, (7, 7), 0) # aplica blur

(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)

cv2.imwrite("pedestrian_test_binarizacao.png", bin)

(T, binI) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY_INV)

cv2.imwrite("pedestrian_test_binarizacao_inv.png", binI)

resultado = np.vstack([
    np.hstack([suave, bin]),
    np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])
])

cv2.imshow("Binarização da imagem", resultado)
cv2.waitKey(0)

cv2.imwrite("pedestrian_test_binarizacao_bitwise.png", cv2.bitwise_and(img, img, mask = binI))
