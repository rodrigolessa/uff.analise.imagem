import cv2
import numpy as np

imgName = 'pedestrian_test.tif'
clip_limit = 3

image = cv2.imread(imgName)
# convert image to LAB color model
image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# split the image into L, A, and B channels
l_channel, a_channel, b_channel = cv2.split(image_lab)

# apply CLAHE to lightness channel
clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(8, 8))
cl = clahe.apply(l_channel)

# merge the CLAHE enhanced L channel with the original A and B channel
merged_channels = cv2.merge((cl, a_channel, b_channel))

# convert iamge from LAB color model back to RGB color model
final_image = cv2.cvtColor(merged_channels, cv2.COLOR_LAB2BGR)
#return cv2_to_pil(final_image) 

res = np.hstack((image, final_image))
#cv2.imwrite('res.png', res)
cv2.imshow("Equalization", res)
cv2.waitKey(0)

cv2.destroyAllWindows()