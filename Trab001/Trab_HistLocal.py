import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
from skimage import data
from skimage.util.dtype import dtype_range
from skimage.util import img_as_ubyte, img_as_float
from skimage import exposure
from skimage.morphology import disk
from skimage.filters import rank
from skimage import io
import os
from scipy import misc
from skimage import data
from skimage import feature


img =(io.imread('lena_B.png', as_grey=True))

# Equalization
img_eq = rank.equalize(img, selem=disk(20))

io.imsave('EqLocal.png', img_eq)

####################################################################################
####################################################################################
####################################################################################
