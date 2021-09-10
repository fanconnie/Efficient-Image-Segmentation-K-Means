
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
			cent2 =	rand_points[1]
		else:
			#print '\n selecting centroid values'
			cent1 = centroid1_avg
			cent2 = centroid2_avg

		#print histogram
		point1_centroid = []
		point2_centroid = []
		w1_centroid = []
		w2_centroid = []
		sum1 = 0
		sum2 = 0
		for i,val in enumerate(histogram):
			''' computing absolute distance from each of the cluster and assigning it to a particular cluster based on distance'''
			#print '\n\n','i',i,'val',val,'cent1', cent1,'cent2', cent2 
			if  abs(i - cent1) <  abs(i - cent2):
				point1_centroid.append(i)
				w1_centroid.append(val)
				sum1 = sum1 + (i * val)
				#print '\nselection 1'
			else:
				point2_centroid.append(i)
				w2_centroid.append(val)
				sum2 = sum2 + (i * val)
				#print '\nselection 2'
		
		
		centroid1_avg = int(sum1)/sum(w1_centroid)	
		centroid2_avg = int(sum2)/sum(w2_centroid)			
		#print '\n\n','sum1',sum1,'sum2',sum2,'cent1', centroid1_avg,'cent2', centroid2_avg
	return [point1_centroid,point2_centroid] 

res = kmeans(hist)
#print res

end = np.zeros((rows,columns))
