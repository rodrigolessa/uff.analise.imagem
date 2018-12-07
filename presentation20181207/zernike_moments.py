# import the necessary packages
import mahotas as mh
 
class ZernikeMoments:
	def __init__(self, radius):
		# Store the size of the radius that will be
		# used when computing moments
		self.radius = radius
 
	def describe(self, image):
		# Return the Zernike moments for the image
		# http://mahotas.readthedocs.io/en/latest/api.html#mahotas.features.zernike_moments
		# mahotas.features.zernike_moments(im, radius, degree=8, cm={center_of_mass(im)})
		return mh.features.zernike_moments(image, self.radius)

# Load one of the demo images
#im = mh.demos.load('nuclear')

# Automatically compute a threshold
#T_otsu = mh.thresholding.otsu(im)

# Label the thresholded image (thresholding is done with numpy operations
#seeds,nr_regions = mh.label(im > T_otsu)

# Call seeded watershed to expand the threshold
#labeled = mh.cwatershed(im.max() - im, seeds)