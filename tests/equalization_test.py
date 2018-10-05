import cv2
import numpy as np
from matplotlib import pyplot as plt

imgName = 'pedestrian_test.tif'

# = 0 Return a grayscale image.
# < 0 Return the loaded image as is (with alpha channel).
img = cv2.imread(imgName, 0)

#cv2.imshow("Original", img)
#cv2.waitKey(0)

# Qualizando imagem pelo histograma
h_eq = cv2.equalizeHist(img)

plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(h_eq.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()

#stacking images side-by-side
res = np.hstack((img, h_eq))
#cv2.imwrite('res.png', res)
cv2.imshow("Equalization", res)
cv2.waitKey(0)

cv2.destroyAllWindows()