
import math 
from PIL import Image
from pylab import *
import matplotlib.cm as cm
import scipy as sp
import random

im = Image.open('input1.jpg').convert('L')
arr = np.asarray(im)

out = Image.open('out1.jpg').convert('L')
arr_out = np.asarray(out)

rows,columns = np.shape(arr)

rand_points = [ random.randint(0, 255) for i in range(2) ]

'''finding the histogram of the image to obtain total number of pixels in each level'''

hist,bins = np.histogram(arr,256,[0,256])

#print hist,bins

centroid1_avg = 0
centroid2_avg = 0
def kmeans(histogram):
	for k in range(0,10):
		print '\niteration',k
		''' First iteration assign random centroid points '''
		if k == 0:
			cent1 = rand_points[0]