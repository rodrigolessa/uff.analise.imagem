import os
import argparse
import cv2
import numpy as np
from shapeIdentify import *
from normalization import Normalizer
import imutils


def display(img, im):
    cv2.imshow(img, im)
    cv2.waitKey(0)


def scale(image, size):
    new = imutils.resize(image, height=size)
    if new.shape[1] > size:
        new = imutils.resize(image, width=size)
    return new


def remove_contour(c, cnts, h, shape, color):

    new = np.full(shape, 255, np.uint8)

    parent = -1

    for i in range(len(cnts)):#-1, 0, -1):
        if h[0][i][3] != parent:
            color = 255 - color
            parent = h[0][i][3]

        if i != c:
            cv2.drawContours(new, [cnts[i]], -1, color, thickness=cv2.FILLED)

    if all(all(p == 255 for p in line) == True for line in new):
        return None
    
    return new



# Parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imgs_folder" , required = True, help = "Images folder")
args = vars(ap.parse_args())
imgs_folder = args['imgs_folder']

N = Normalizer(170)

for img in os.listdir(imgs_folder):

    image = cv2.imread("{}/{}".format(imgs_folder, img),0)

    display("original", image)
    
    thresh = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY)[1]

    _, cnts, h = cv2.findContours(thresh.copy(), cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE)

    # Hierarchy: For each contour -> [next, previous, child, parent]
    n = h[0][0][2]  # first child
    c = []  # c -> external contours [contour, area, id]
    while(n > 0): 
        c.append([cnts[n], cv2.contourArea(cnts[n]), n])
        n = h[0][n][0]

    if len(c) > 1:
        c = sorted(c, key=lambda x: x[1], reverse=True)

    if h[0][c[0][2]][2] != -1:
        new = np.full(image.shape, 255, np.uint8)
        cv2.drawContours(new, [c[0][0]], 0, 0, thickness=cv2.FILLED)

        shape = detectShape(c[0][0], new)

        if shape != "unknown":  # if is a common shape, remove it
            print(shape)

            new = remove_contour(c[0][2], cnts, h, image.shape, 255)

            if not new is None:
                image = new

    display("mod", image)