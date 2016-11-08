from PIL import Image
import numpy

#########
tamanho = 10.0
ondas = 9.0
freq = 1.0
########

im = Image.open('lena_B.png')

m = numpy.asarray(im)
m2 = numpy.zeros((im.size[0],im.size[1],3))
width = im.size[0]
height = im.size[1]

A = m.shape[0] / tamanho
w = ondas / m.shape[1]

shift = lambda x: A * numpy.sin(freq*numpy.pi*x * w)

for i in range(m.shape[0]):
    m2[:,i] = numpy.roll(m[:,i], int(shift(i)))

im2 = Image.fromarray(numpy.uint8(m2))
im2.save('TransNaoLinearDistorcao.png')
