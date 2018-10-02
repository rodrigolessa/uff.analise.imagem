import cv2
import numpy as np
from matplotlib import pyplot as plt

imgName = 'pedestrian_test.tif'

# = 0 Return a grayscale image.
# < 0 Return the loaded image as is (with alpha channel).
# img = cv2.imread('pedestrian_test.tif', 0)
img = cv2.imread(imgName)

cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)

cv2.waitKey(0)
cv2.destroyAllWindows()