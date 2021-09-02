
import math 
from PIL import Image
from pylab import *
import matplotlib.cm as cm
import scipy as sp
import random

im = Image.open('input1.jpg').convert('L')
arr = np.asarray(im)