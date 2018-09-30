import cv2
import numpy as np

imgName = 'pedestrian_test.tif'

img = cv2.imread(imgName, 0)

#CLAHE (Contrast Limited Adaptive Histogram Equalization)

# create a CLAHE object (Arguments are optional).
#clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe = cv2.createCLAHE()
cl1 = clahe.apply(img)

#cv2.imwrite('clahe_2.jpg',cl1)

res = np.hstack((img, cl1))
#cv2.imwrite('res.png', res)
cv2.imshow("Equalization", res)
cv2.waitKey(0)

cv2.destroyAllWindows()