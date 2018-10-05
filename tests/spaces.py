import cv2
import numpy as np
from matplotlib import pyplot as plt

imgName = 'pedestrian_00013.png'

img = cv2.imread(imgName)

cv2.imshow("Original", img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.imwrite('pedestrian_00013_gray.png', gray)
cv2.waitKey(0)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.imwrite('pedestrian_00013_hsv.png', hsv)
cv2.waitKey(0)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)
cv2.imwrite('pedestrian_00013_lab.png', lab)
cv2.waitKey(0)

yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
cv2.imshow("YUV", yuv)
cv2.imwrite('pedestrian_00013_yuv.png', yuv)
cv2.waitKey(0)

cv2.destroyAllWindows()