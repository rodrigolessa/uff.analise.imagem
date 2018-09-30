import cv2
 
img = cv2.imread('pedestrian_test.png')
img_shape = img.shape
height = img_shape[0]
width = img_shape[1]
 
for row in range(width):
    for column in range(height):
        print (img[column][row])