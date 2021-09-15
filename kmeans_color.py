
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