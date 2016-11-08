# By Marlon H, Gustavo Diel (cc) with <3

from PIL import Image
import matplotlib.pyplot as plt
from numpy import *
from math import log
from math import sqrt

# Leitura da imagem

im1 = Image.open('lena_B.png')#('marilyn.jpg')
(l,h) = im1.size
out = Image.new(im1.mode, (l,h))

# Histograma
histograma = im1.histogram()
histr = range(0,256)
histg = range(0,256)
histb = range(0,256)

for i in range(0,256):
    histr[i] = histograma[i];
    histg[i] = histograma[i+256];
    histb[i] = histograma[i+256*2]+2;


#plt.plot(histr)
#plt.ylabel('Histograma')
#plt.show()



# Exponencial
out = Image.new(im1.mode, (l,h))
def expf(x):
    x = x/256.0
    return int((x*x)*256)


for i in range(0,l):
   for j in range(0,h):
       r = expf(im1.getpixel((i,j))[0])
       out.putpixel((i,j),(r,r,r))

out.save("out2.png");

# Linear
out = Image.new(im1.mode, (l,h))
def linearf(x):
    x = x/256.0
    return int((1.3*x)*256)


for i in range(0,l):
   for j in range(0,h):
       r = linearf(im1.getpixel((i,j))[0])
       out.putpixel((i,j),(r,r,r))

out.save("out3.png");



# Equalizacao do Histograma

import operator

def equalize(h):
    lut = []
    for b in range(0, len(h), 256):
        step = reduce(operator.add, h[b:b+256]) / 255
        n = 0
        for i in range(256):
            lut.append(n / step)
            n = n + h[i+b]
    return lut

im = Image.open("lena_B.png")
lut = equalize(im.histogram())
im = im.point(lut)
im.save("out4.png");
