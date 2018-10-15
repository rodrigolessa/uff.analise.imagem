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
		# Parameters:
		# 	im : 2-ndarray
		# 		input image
		# 	radius : integer
		# 		the maximum radius for the Zernike polynomials, in pixels. 
		# 		Note that the area outside the circle (centered on center of mass) 
		# 		defined by this radius is ignored.
		# 	degree : integer, optional
		# 		Maximum degree to use (default: 8)
		# 	cm : pair of floats, optional
		# 		the centre of mass to use. By default, 
		# 		uses the image’s centre of mass.
		# Returns:
		# 	zvalues : 1-ndarray of floats
		return mh.features.zernike_moments(image, self.radius)