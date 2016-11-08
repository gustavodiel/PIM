from PIL import Image
import numpy
from scipy.ndimage import filters
import os
import matplotlib.pyplot
import glob
import time

files =  glob.glob("*.py")


for file in files:
    if file == 'Trab_CriaHisto.py' or file == 'Executa.py':
        continue

    print("Executando {}".format(file))
    start_time = time.time()
    execfile(file)
    print("--- %s segundos ---\n" % (time.time() - start_time))

execfile('Trab_CriaHisto.py')
####################################################################################
####################################################################################
####################################################################################
