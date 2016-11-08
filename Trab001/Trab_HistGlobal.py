# By Marlon H, Gustavo Diel (cc) with <3

from PIL import Image
import matplotlib.pyplot as plt
from numpy import *
from math import log
from math import sqrt
import operator

# Equalizacao do Histograma
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
im.save("EqGlobal.png")
