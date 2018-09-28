import os
import sys
import cv2
import glob
import numpy as np
import argparse
from matplotlib import pyplot as plt

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", required = True, help = "Path to where the files has stored")
ap.add_argument("-e", "--extension", required = True, help = "Image type")
ap.add_argument("-d", "--destination", required = True, help = "Path to store new images")

args = vars(ap.parse_args())

imageFolder = args["folder"]
imageExtension = '.' + args["extension"].lower()
imageDestination = '.' + args["destination"]
imageFinder = '{}/*{}'.format(imageFolder, imageExtension)

try:
    os.remove(imageDestination)
except OSError:
    pass

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

imagesInFolder = glob.glob(imageFinder)

qt = len(imagesInFolder)

i = 1

# Loop over the sprite images
for spritePath in imagesInFolder:

	# Extract image name, this will serve as unqiue key into the index dictionary.
	imageName = spritePath[spritePath.rfind('\\') + 1:].lower().replace(imageExtension, '')

	# Try to manipulate the image if it is possible
	try:
		progress(i, qt)

		# then load the image.
		#5 img = cv2.imread('wiki.jpg',0)
		image = cv2.imread(spritePath)



		i+=1

	except:
		pass


    
    
#    6 
#    7 hist,bins = np.histogram(img.flatten(),256,[0,256])
#    8 
#    9 cdf = hist.cumsum()
#   10 cdf_normalized = cdf * hist.max()/ cdf.max()
#   11 
#   12 plt.plot(cdf_normalized, color = 'b')
#   13 plt.hist(img.flatten(),256,[0,256], color = 'r')
#   14 plt.xlim([0,256])
#   15 plt.legend(('cdf','histogram'), loc = 'upper left')
#   16 plt.show()