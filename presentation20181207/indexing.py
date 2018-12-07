# Indexing the dataset by quantifying each image in terms of shape.
# Apply the shape descriptor defined to every sprite in dataset.
# Frist we need the outline (or mask) of the object in the image 
# prior to applying Zernike moments. 
# In order to find the outline, we need to apply segmentation

# Import the necessary packages
from zernike_moments import ZernikeMoments
# Just for debugging purposes
from PIL import Image as pim
import numpy as np
import cv2
import pickle as cp
import glob
 

imageFolder = 'segmentation'
imageExtension = '.png'
imageFinder = '{}/*{}'.format(imageFolder, imageExtension)
imageMomentsFile = 'index.pkl'
imageDebug = 'pet_view_008_frame114' #'segmentation_pedestrian_frame60'
index = {}

# Initialize descriptor with a radius of 21 pixels, 
# used to characterize the shape of object
zm = ZernikeMoments(21)

# Time to quantify sprites:

# Loop over the sprite images
for spritePath in glob.glob(imageFinder):
	# Extract image name, this will serve as unqiue key into the index dictionary.
	# Parse out the image name,
	# \\ using double address bar on Windows
	# / address bar on Linux
	imageName = spritePath[spritePath.rfind('\\') + 1:].replace(imageExtension, '')
	
	# then load the image.
	image = cv2.imread(spritePath)

	# Debugging: show original image
	if imageName.find(imageDebug) >= 0:
		cv2.imshow('original', image)
		cv2.waitKey(0)

	# Convert it to grayscale
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# First, we need a blank image to store outlines
	# we appropriately a variable called outline 
	# and fill it with zeros with the same width and height as the sprite image.

	# Accessing Image Properties
	# Image properties include number of rows, columns and channels, 
	# type of image data, number of pixels etc.
	# Shape of image is accessed by img.shape. It returns a tuple of number of rows, 
	# columns and channels (if image is color):
	outline = np.zeros(image.shape, dtype = "uint8")

	# Initialize the outline image,
	# find the outermost contours (the outline) of the object, 
	# cv2.RETR_EXTERNAL - telling OpenCV to find only the outermost contours.
	# cv2.CHAIN_APPROX_SIMPLE - to compress and approximate the contours to save memory
	img2, contours, hierarchy = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	# Sort the contours based on their area, in descending order. 
	# keep only the largest contour and discard the others.
	contours = sorted(contours, key = cv2.contourArea, reverse = True)[0]

	# The outline is drawn as a filled in mask with white pixels:
	cv2.drawContours(outline, [contours], -1, 255, -1)

	# Debugging: just outline of the object
	if imageName.find(imageDebug) >= 0:
		cv2.imshow('outline', outline)
		cv2.imwrite('outline.png', outline)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	# Compute Zernike moments to characterize the shape of object outline
	moments = zm.describe(outline)

	# Debugging: analyse descriptions of form
	if imageName.find(imageDebug) >= 0:
		print(moments.shape)
		print('{}: {}'.format(imageName, moments))

	# then update the index
	index[imageName] = moments


# cPickle for writing the index in a file
with open(imageMomentsFile, "wb") as outputFile:
	cp.dump(index, outputFile, protocol=cp.HIGHEST_PROTOCOL)