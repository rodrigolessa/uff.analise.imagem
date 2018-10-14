# Indexing the dataset by quantifying each image in terms of shape.
# Apply the shape descriptor defined to every sprite in dataset.
# Frist we need the outline (or mask) of the object in the image 
# prior to applying Zernike moments. 
# In order to find the outline, we need to apply segmentation

# Import the necessary packages
from zernike_moments import ZernikeMoments
#from PIL import Image as pim
##logo.thumbnail(logo.size)
##logo.save('my-image.png')
import numpy as np
import cv2
import pickle as cp
import glob

class MainIndexing:

    def __init__(self):
        # Initializing
        self.imageMomentsFile = 'index.pkl'
        self.index = {}
        # Initialize descriptor with a radius of 21 pixels
        self.zm = ZernikeMoments(21)

        # If index file exists, try to delete
        try:
            os.remove(self.imageMomentsFile)
        except OSError:
            pass

    def ExtractShape(self, imgPath):
        # Extract image name, this will serve as unqiue key into the index dictionary
        imgName = ''#imgPath[spritePath.rfind('\\') + 1:].replace(imageExtension, '')
        
        # then load the image.
        img = cv2.imread(imgPath)

        # Pad the image with extra white pixels to ensure the
        # edges of the object are not up against the borders
        # of the image
        #image = cv2.copyMakeBorder(image, 15, 15, 15, 15, cv2.BORDER_CONSTANT, value = 255)

        # Debugging: Show Original
        cv2.imshow('original', img)
        cv2.waitKey(0)

        ######################################################
        # Espaços de cores da imagem

        ######################################################
        # Canais da Imagem

        # Convert it to grayscale
        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Debugging: Show converted,one chanel with  intensity
        cv2.imshow('gray', grayscale)
        cv2.waitKey(0)

        ######################################################
        # Filtros para remover ruídos

        # Apply a blur filter to reduce noise
		blur = cv2.medianBlur(grayscale, 5)

		# Bilateral Filter can reduce unwanted noise
		blur = cv2.bilateralFilter(grayscale, 9, 75, 75)

        #cv2.imwrite(os.path.join(debugPath , '{}_blur.png'.format(imageName)), blur)

        ######################################################
        # Inverter intensidades
    
        # For segmentation: Flip the values of the pixels 
        # (black pixels are turned to white, and white pixels to black).
        inv = cv2.bitwise_not(blur)

        # Debugging: Invert image
        cv2.imshow('inverted', inv)
        cv2.waitKey(0)

        ######################################################
        # Limiar na imagem

        # Then, any pixel with a value greater than zero (black) is set to 255 (white)
        #inv[inv > 0] = 255
        #thresh = inv

		# Then, any pixel with a value greater than zero (black) is set to 255 (white)
		# NOTE: First version
		#thresh[thresh > 0] = 255
		# NOTE: Second version
		# THRESH_BINARY = fundo preto or THRESH_BINARY_INV = fundo branco
		# Then, any pixel with a value greater than zero (black) is set to 255 (white)
		_, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Debugging: Threshold it
        cv2.imshow('thresholded', thresh)
        cv2.waitKey(0)

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
        img2, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Sort the contours based on their area, in descending order. 
        # keep only the largest contour and discard the others.
        contours = sorted(contours, key = cv2.contourArea, reverse = True)[0]

        # The outline is drawn as a filled in mask with white pixels:
        cv2.drawContours(outline, [contours], -1, 255, -1)

        # Debugging: just outline of the object
        cv2.imshow('outline', outline)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Compute Zernike moments to characterize the shape of object outline
        moments = self.zm.describe(outline)

        # then update the index
        #self.index[imageName] = moments

        # cPickle for writing the index in a file
        #with open(imageMomentsFile, "wb") as outputFile:
	        #cp.dump(index, outputFile, protocol=cp.HIGHEST_PROTOCOL)



mi = MainIndexing()
mi.ExtractShape('pedestrian_test_60.jpg')