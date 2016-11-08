from PIL import Image
import numpy as np
from scipy.ndimage import filters


img = Image.open('lena_B.png')
(l,h) = img.size
out = Image.new('L', (l,h))
def linearf(x, i, j):
    return x, j, i


for i in range(0,l):
   for j in range(0,h):
       pix, px, py = linearf(img.getpixel((i,j))[0], i, j)
       out.putpixel((px,py),pix)


out.save('TransLinearRot.png')

out = Image.new('L', (l,h))
def linearf(x, i, j):
    x = (2*x + 47) / 3
    return int(x), i, j


for i in range(0,l):
   for j in range(0,h):
       pix, px, py = linearf(img.getpixel((i,j))[0], i, j)
       out.putpixel((px,py),pix)


out.save('TransLinearSimples.png')
####################################################################################
####################################################################################
####################################################################################
