
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


shape = np.shape(arr)

rows = shape[0]
columns = shape[1]

'''obtaining 6 random centroid points'''

r_points = [ random.randint(0, 255) for i in range(6) ]
g_points = [ random.randint(0, 255) for i in range(6) ]
b_points = [ random.randint(0, 255) for i in range(6) ]

grey_l = defaultdict(list)

''' Grey scale levels corresponding to 6 clusters'''

grey1 = 40
grey2 = 80
grey3 = 120
grey4 = 160
grey5 = 200
grey6 = 240

grey_l[0] = 40
grey_l[1] = 80
grey_l[2] = 120
grey_l[3] = 160
grey_l[4] = 200
grey_l[5] = 240



g = defaultdict(list)

g2 = []
g3 = []
g4 = []
g5 = []
g6 = []

end = np.zeros((rows,columns))
zavg = [0,0,0]	
