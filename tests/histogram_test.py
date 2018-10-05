import cv2
import numpy as np
from matplotlib import pyplot as plt

imgName = 'pedestrian_test.tif'

# = 0 Return a grayscale image.
# < 0 Return the loaded image as is (with alpha channel).
# img = cv2.imread('pedestrian_test.tif', 0)
img = cv2.imread(imgName)

# We have three channels (RGB) for each pixel and 
# we cannot apply histogram equalization on the three channels 
# in a separate manner.

# Convert image to the grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Outro espaço de cor YUV de TVs antigas
#img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

cv2.imshow("RGB to grayscale", gray)
cv2.waitKey(0)

hist, bins = np.histogram(gray.flatten(), 256, [0, 256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(gray.flatten(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc = 'upper left')
plt.show()
plt.close()

## Equalizando por mascara
#cdf_m = np.ma.masked_equal(cdf,0)
#cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
#cdf = np.ma.filled(cdf_m,0).astype('uint8')
## Imagem qualizada
#img2 = cdf[img]

#img3 = cv2.imread(imgName, 0)
#equ = cv2.equalizeHist(img3)
##stacking images side-by-side
#res = np.hstack((img3, equ))
##cv2.imwrite('res.png', res)
#cv2.imshow("Equalization", res)
#cv2.waitKey(0)

##img[:,:,0] = cv2.equalizeHist(img[:,:,0])
##img = cv2.equalizeHist(img)

##hist_equalization_result = cv2.cvtColor(img, cv2.COLOR_YUV2BGR)

##cv2.imshow("Equalization", hist_equalization_result)
##cv2.waitKey(0)

cv2.destroyAllWindows()