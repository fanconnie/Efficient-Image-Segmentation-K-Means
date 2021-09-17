
import math 
from PIL import Image
from pylab import *
import matplotlib.cm as cm
import scipy as sp
import random
from collections import defaultdict
import operator

im = Image.open('input2.jpg')
arr = np.asarray(im)

out = Image.open('out2.jpg').convert('L')
arr_out = np.asarray(out)

rows,columns = np.shape(arr_out)
print 'background pixel level',arr_out[0][0]

#print '\nrows',rows,'columns',columns
ground_out = np.zeros((rows,columns))


''' Converting ground truth image into binary image for evaluation'''

for i in range(rows):
	for j in range(columns):
		if arr_out[i][j] > 120:
			ground_out[i][j] = 0

		else:
			ground_out[i][j] = 1

plt.figure()
plt.imshow(ground_out, cmap="Greys_r")
plt.show()

