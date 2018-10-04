import cv2
import numpy as np
from matplotlib import pyplot as plt

imgName = 'pedestrian_00013.png'

img = cv2.imread(imgName)

#cv2.imshow("Original", img)

(blue, green, red) = cv2.split(img)

cv2.imshow("blue", blue)
cv2.imwrite('pedestrian_00013_blue.png', blue)
cv2.waitKey(0)

cv2.imshow("green", green)
cv2.imwrite('pedestrian_00013_green.png', green)
cv2.waitKey(0)

cv2.imshow("red", red)
cv2.imwrite('pedestrian_00013_red.png', red)
cv2.waitKey(0)

cv2.destroyAllWindows()