from PIL import Image
import numpy
from scipy.ndimage import filters
import os
import matplotlib.pyplot
import glob

files =  glob.glob("*.png")


for file in files:
    matplotlib.pyplot.clf()
    print("Trabalhando no arquivo {}!".format(file))
    try:
        img=Image.open(file).convert(mode="L")
    except:
        print("Arquivo nao existe!")
        exit()

    pixels=numpy.array(img.getdata())

    x=range(256)
    for i in pixels:
        x[i]+=1

    matplotlib.pyplot.bar(range(0,256),x,color='k')
    matplotlib.pyplot.title("Histograma")
    matplotlib.pyplot.xlabel("Cinza")
    matplotlib.pyplot.ylabel("Qnt pixels")
    matplotlib.pyplot.savefig('Histo_{}.jpg'.format(file))
    matplotlib.pyplot.clf()

####################################################################################
####################################################################################
####################################################################################
